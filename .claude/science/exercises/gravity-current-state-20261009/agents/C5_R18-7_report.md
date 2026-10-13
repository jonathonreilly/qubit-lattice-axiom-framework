# C5 round 18, probe R18-7: set A's completion N as a construction (worker report)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-13, 02:43Z to about 03:12Z. No repository file was edited.

**Scratch:** `scratchpad/C5/R18-7/`.
- `r187_ll.py` / `r187_ll.out`: sections [1]-[2] (sympy: Landau–Lifshitz field stress, O(M²) point mass, β).
- `r187_lapse.py` / `r187_lapse.out`: section [1b] (sympy: static lapse identity).
- `r187_checks.py` / `r187_checks.out`: sections [3]-[8] (numerics). Runtime about 25 s with OMP_NUM_THREADS=2. `r187_checks.err` holds only scipy quadrature warnings from [3].
- SHA-256 prefixes: `r187_ll.py` cd3e5028…, `.out` 48c6916b…; `r187_lapse.py` b9f87947…, `.out` af3fbdb2…; `r187_checks.py` c80a854e…, `.out` 24ac4c0b….
- `rerun/`: copies of the archived R16-14, R16-4, R15-2 and R13-6 runners. **All four rerun byte-identical** with their archived `.out` files (checked; `diff` empty).
- No downloads, no web fetches. Literature is labelled RECALLED.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `vR16-14` = `P/agents/C5_R16-14_referee_verdict.md` (and so on); `R16-14:n` = `P/agents/C5_R16-14_report.md:n` (and so on); `S23` = `P/agents/C5_S23_synthesis.md`; `ll:n`, `lapse:n`, `out:n` = line n of `r187_ll.out`, `r187_lapse.out`, `r187_checks.out`.

**What I read.** In full: `AX`; `TESTS:2302-2320` (C5 method); the set-A entries and verdicts `TESTS:3143-3175, 3405-3418, 4218-4243, 4320-4330, 4436-4470, 4515-4527, 4682-4733, 4815-4830, 4888-4897, 4939-4968, 5108-5135, 5170-5195, 5280-5300, 5430-5449, 5628-5685, 5870-5900, 5996-6018`; item R18-7 `TESTS:6682-6736`. The reports and verdicts `C5_R16-14_report.md` (all), `vR16-14`, `C5_R16-14_referee.md`, `C5_R15-2_report.md` (all), `vR15-2`, `vR13-6`, `vR16-4`, `vR12-4`, `vR6-4`, `vR14-2`; `C5_R13-6_report.md:1-60, 140-300`; `S23:240-275, 640-650` and grep hits for P88/P107.

**Labels.** **proved** (derived here under stated hypotheses); **checked** (a number in my `.out` files); **suggested** (argued, not proved); **reading** (interpretation); **comparator** (literature, RECALLED or via an earlier referee). **Order rule:** O(G) mean field plus all O(G²) terms in the static sector for β; Gaussian (second order in the matter–meter coupling) for CP; O(G·noise²) for the noise-fed mean.

---

## Reading against the FIXED readings (`TESTS:6730-6733`)

**Worker reading: CONSTRUCTED, in a stated scope.** The law is E1 + N_c, given in §3. A referee is recommended but not required, since this is not a FAIL or no-go.

**Scope:**
- static and quasi-static sectors at O(G²);
- weak field;
- the meter is the finite rational network that R13-6 already calls the explicit model (`R13-6:244`);
- the O(G²) readout is posed in the CMB frame's harmonic gauge.

| Clause of CONSTRUCTED | Result | Label |
|---|---|---|
| explicit E1 + N law at O(G²) | E1 + N_c (§3). This is N with four named specifications: (1) the realised field, not the mean field; (2) the record densitised on the classical side, τ = (−g)(J + t_LL) + t_H, so a = 4; (3) a causal conserving projection Π; (4) harmonic gauge, with P76 and P88 initial data | proved (construction) |
| well-posed readout | At each order h is a retarded solution of a flat wave equation. Its source is a known functional of the records and of lower orders. The data are fixed by P76 plus P88 (extended to the residual harmonic gauge modes). The noise is finite at every age. | proved; perturbative validity at t_H suggested |
| CP at Gaussian order | The quantum instrument is literally R13-6/R15-2's, because with a = 4 the meter still measures T. N enters only through classical post-processing and a record-controlled feedback unitary. So R13-6's CP proof (`R13-6:281-290`) carries over unchanged. A toy model checks this: the Choi matrix is PSD (out:52). | proved for finite rational networks; checked (toy) |
| β = γ = 1 | γ = 1 is inherited at O(G) (`vR16-14:5`). β = 1: by the LL identity, the readout metric solves Einstein's equations with a conserved effective source, so the static exterior is GR at O(G²). A sympy check gives β = 1 exactly for a point mass (ll:12-16). The smeared source differs from GR only by erfc tails (out:12-13), plus 4ℓ²M²/r⁴ if Λ is also filtered (out:8-9). | proved; checked |
| noise kernel intact | At O(G) it is identical: h₁ is E1's. At O(G²) the instrument is unchanged. But the S/V metric noise is held in harmonic, not Poisson, gauge (see caveat 1). | proved at O(G); see caveat |

**Caveats, which bound the CONSTRUCTED reading:**
1. **Gauge conflict with P-r15b (`R15-2:133-135, 257`).**
   - The LL relaxed equations need harmonic gauge. There the realised S/V record noise has secularly growing pure-gauge parts: per mode up to R = 7e28 (drag ceiling) to 2.8e35 (strict, ℓ = 4e-10 m) times the Poisson-gauge field at t_H (checked out:39-47).
   - The static active noise density computed below is invariant under a change of spatial gauge (checked [1b]).
   - The time-dependent noise-fed O(G²) terms are **not** computed gauge-invariantly.
   - If a referee holds that "noise kernel intact" includes R15-2's Poisson-gauge record, the reading is OPEN, because the Poisson-gauge O(G²) law is not built.
2. **Exact irrational-limit CP** stays conditional, as in `vR15-2:15`. The explicit model is the rational approximant with Γ_min ≤ 1/t_H (`R13-6:244`).
3. **Lemma CU** still holds only inside its ansatz (`vR15-2:7`).
4. **Π's freedom.** Π is non-unique up to a conserved tensor. That gives an O(G²)(ℓ/R)² non-PPN ambiguity, localised in the body.
5. **Excluded:** strong field (neutron-star coefficients), E2, and the V, T_⊥ and TT channels in the noise-fed mean.

**Against the expectation (`TESTS:6736`).**
- "CONSTRUCTED at O(G²) with the gauge dependence of the LL source as the main caveat": **confirmed**, with two additions:
  - N as R16-14 wrote it does not close (§4.1). Closing it needs Π.
  - The gauge caveat is concrete: secular pure-gauge S/V noise in harmonic gauge.
- "Premise (iii) forced": **only qualitatively.** The realised noise field must enter the O(G²) source, because CP excludes the mean-field N̄ (§5). But the **local active density** of the static scalar noise is (2a − 8)|u₁|, set by how the noise enters (checked, gauge-invariant). If R13-6/R15-2's meter is kept unchanged (it measures T) and the classical side forms τ = (−g)(J + t_LL) + t_H, then a = 4 and it is **zero** (out:26-37). This is a reading of N (R16-14's "F·τ" does not say where the noise enters); a meter that measures (−g)T instead gives a = 0 and −8|u₁|. So in this scope R15-2's constraint-energy overshoot is not forced back for Mercury-type tests. The LL "energy density" is +|u₁| at a = 4, but energy density is definition-dependent: the relevant cosmological average is not built here.

---

## 0. In plain words

- **The question.** R16-14 showed that a metric linear in matter records gets Mercury wrong. Its fix, completion N, was: let gravity's own energy also source the metric record. Can that fix be turned into an actual law?
- **Mostly yes, at second order.** Three things had to be added.
  1. **N as written does not hang together.** The record smooths matter's stress over the length ℓ, but matter falls in the real field. Gravity's own stress then does not exactly balance the smoothed matter, and the leftover is a small source that breaks conservation, of relative size (ℓ/R)² (checked: about 1.4(ℓ/R)², out:19-21). The fix is a fixed causal rule (Π) that completes the recorded source so that it is conserved, as R15-2 already did for the noise. The metric then obeys Einstein's equations with a recorded source, and the Sun's outside field is GR's, so β = 1.
  2. **Gravity's energy must be computed from the actual field, not its average.** An average-field rule would make the quantum dynamics depend nonlinearly on the state. Such a map is not a legitimate (CP) quantum operation (checked in a toy, out:53-54). So the realised-field version is the only one of R16-14's two options that keeps CP.
  3. **Gauge.** Gravity's "own energy" (the LL pseudotensor) depends on the coordinates. In the coordinates where the LL equations are simplest, the record's Newtonian-type noise has huge coordinate wobbles that grow with time. The coordinate-free static part is fine; the time-dependent part is not worked out.
- **Does the noise's field energy now have to gravitate (premise (iii))?** Partly.
  - Its field energy does enter the equations.
  - But for the reading of N that keeps the old meter unchanged, the static Newtonian noise pulls on Mercury with **zero** net strength at this order. The noise "mass" sits in its own potential wells, and its field energy cancels that exactly (checked: −0.0000|u₁|, out:35).
  - Other ways of inserting the noise give −8|u₁| or +4|u₁|.
  - So the size of premise (iii) is a choice made by the law, not a consequence of N.
- **An aside.** "Linear in records" depends on which metric variable is linear.
  - Linear metric: β = 0 (R16-14).
  - Linear Landau–Lifshitz density variable: β = 3, a third of GR's perihelion advance (checked, ll:17).
  - Both are wrong. Only the self-sourced version gives β = 1.

---

## 1. Prior art (each counted once)

1. **R16-14 and its verdict.**
   - Lemma L: L₀ gives β = 0, L½ gives β_eff = ½ (`vR16-14:13`).
   - N formally restores β = 1 but is a new, uncompleted nonlinear bridge. N needs quadratic backreaction of the realised field, but does not establish premise (iii) (`vR16-14:15`).
   - R16-14 asserted "Bianchi holds at O(G²) because F commutes with ∂ and ∂·τ = 0" (`R16-14:152`). The referee qualified this: commutation preserves conservation only "if a conserved total source already exists" (`C5_R16-14_referee.md:16`).
   - N̄ is "in tension with AX:82-83" (`R16-14:161`).
2. **R15-2 and its verdict.**
   - Lemma A: only TT has the cone pole (`vR15-2:5`).
   - Conserved noise needs f(0) = f′(0) = 0 (`vR15-2:9`).
   - Lemma B and the B term, P76 (`vR15-2:11`).
   - CP is proved for finite rational networks; the irrational limit is conditional (`vR15-2:15`).
   - |u₁| = ħI_F/(32π^{3/2}ℓ³τ) with I_F = 21/32; premise (iii) not established (`vR15-2:17`).
   - The record is held in Poisson gauge (P-r15b, `R15-2:133-135`). The second-order covariant conservation "not covered"; a ξ⁽²⁾ with nonzero mean is suggested (`R15-2:189`).
3. **R13-6.**
   - E1-H1–H5 (`R13-6:146-157`).
   - The explicit model is the rational approximant (`R13-6:244`).
   - CP at every finite age (`R13-6:281-290`).
   - "The metric is a linear functional of the records" (`R13-6:442`).
   - Lemma D and the repaired gain P-r13b (`vR13-6:3-15`).
4. **R16-4.** Free TT data are remembered; P88 (h_TT = ḣ_TT = 0, or recorded data) (`vR16-4:17-19`).
5. **R12-4** (`vR12-4:19`): the stationary no-go that forces E1's start. **R6-4** (`vR6-4:7`): the Newtonian window.
6. **S23.**
   - P107 = completion N (`S23:531`).
   - The P107/P88 interlock: under N the readout is fixed by records only together with an initial TT datum (`S23:262, 649`).
7. **Comparators (RECALLED).**
   - The Landau–Lifshitz identity ∂_μ∂_νH^{αμβν} = 2(−g)G^{αβ} + 16πG(−g)t_LL^{αβ}, with H = 𝔤^{αβ}𝔤^{μν} − 𝔤^{αν}𝔤^{βμ} and 𝔤 = √−g g^{··}.
   - The relaxed harmonic-gauge equations □h^{αβ} = −16πGτ^{αβ}, τ = (−g)(T + t_LL) + t_H, and ∂_βt_H^{αβ} = 0 in harmonic gauge (Poisson & Will 2014).
   - Harmonic-coordinate Schwarzschild.
   - The static identity R₀₀ = N D²N.
   - The retarded Green function of □² in 3+1 is θ(t − |x|)/(8π) (causal).
   - Nonlinear (state-dependent) quantum dynamics is not a linear CP map (Gisin 1990; Polchinski 1991).
   - Second-order Poisson-gauge perturbation theory exists (Matarrese–Mollerach–Bruni 1998); it is not used here.
8. **Repository grep** (`P/agents/`, `P/TESTS.md`) for "conserving projection", "commutator", "insertion", "gothic", "β = 3", "lapse equation". There were no hits on these objects. `docs/` was not grepped.

## 2. Hypotheses: class 𝒩 (stated before any title)

- **H1.** E1 as R13-6/R15-2 (`R13-6:146-157`; `R15-2:83-90`):
  - Minkowski background with the CMB frame u;
  - repaired gain F = e^{−k²ℓ²/2}(1 − 4iωτ)(1 − iωτ)^{−4};
  - R15-2's channel meters at the least-decoherence split;
  - a finite start with B (P76);
  - P88 zero TT datum;
  - the meter network rational, with Γ_min ≤ 1/t_H (`R13-6:244`).
- **H2.** Matter is minimally coupled to the readout metric g[h] (full nonlinear H_m[ψ; g]). The feedback uses only past records (G_R(0) = 0; causal F).
- **H3.** The O(G²) readout is posed in harmonic coordinates of the CMB frame (needed for the LL form).
- **H4.** The noise-fed mean is computed for the static (quasi-static) scalar ρ-channel, with a homogeneous Gaussian ensemble.
- **Excluded:** E2; strong field; V, T_⊥ and TT channels in §6; expansion (FRW); non-Gaussian meters.

---

## 3. The law E1 + N_c (explicit)

Gothic variables: 𝔤^{αβ} = √−g g^{αβ} = η^{αβ} − h^{αβ}.

1. **Record (quantum side; unchanged from R13-6/R15-2).**
   - J^{αβ} = F·(T^{αβ} + ξ^{αβ}) plus B^{αβ} (P76). The noise free data are reconstructed by flat conservation (R15-2 §3.3a).
   - The meter measures T, as before. No coefficient depends on h.
2. **Classical source (N, realised field; a = 4).**
   - S^{αβ} := (−g)J^{αβ} + Λ^{αβ}[h], where Λ := (−g)t_LL[h] + t_H[h] is built from the **realised** h. Λ is not filtered: this is choice N₁; choice N_F, which filters Λ, is in §4.2.
3. **Conserving projection Π (new).**
   - τ_rec := S + K, where K is the causal symmetric solution of ∂_βK^{αβ} = −∂_βS^{αβ}.
   - In Fourier, with D^α := ip_βS^{αβ}: K = i(p^αD^β + p^βD^α)/p² − i p^αp^β(p·D)/p⁴, with retarded p⁻² and p⁻⁴.
   - Algebra: ip_βK^{αβ} = −D^α (proved). The retarded □⁻² kernel is supported inside the future cone (comparator), so Π is causal. Π = 1 on conserved S.
4. **Readout.**
   - □h^{αβ} = −16πG τ_rec^{αβ}, retarded from t₀.
   - Data at t₀: the constraint solution for the recorded τ^{0ν}(t₀), which is P76 with Λ^{0ν}(t₀) included. All homogeneous (free) data are zero: P88 extended to the residual harmonic gauge modes.

**Consequence (proved).**
- ∂_βτ_rec = 0, so ∂_βh^{αβ} = 0 holds at every order.
- The LL identity then gives exactly G^{αβ}[g] = 8πG T_eff^{αβ}, with (−g)T_eff := τ_rec − Λ = (−g)J + K.
- So the readout metric **is a GR metric with a recorded, automatically conserved effective source**.
- Order by order:
  - h₁ = −16πG □⁻¹_ret(FT⁽⁰⁾ + Fξ + B): Π acts trivially here, so h₁ is E1's metric exactly;
  - h₂ = −16πG □⁻¹_ret Π[((−g)J)⁽¹⁾ + Λ⁽²⁾[h₁]].

---

## 4. Probe (a): does the O(G²) iteration close?

### 4.1 Literal N does not close (proved; checked out:17-22)

Take N as R16-14 wrote it (`R16-14:143-152`): source F·τ, or F[(−g)T] + Λ, with matter on geodesics of g. Use the LL identity and Bianchi at second order, and write Q^α[h; X] := Γ^α_{βμ}[h]X^{βμ} − X^{αβ}∂_β ln√−g[h]. Then:

  ∂_β τ⁽²⁾ = Q[h₁; F T⁰] − F Q[h₁; T⁰] ≠ 0.

- **Where the defect comes from.** Matter's conservation is ∂((−g)T)⁽¹⁾ = −Q[h₁; T⁰]. The LL stress has ∂Λ⁽²⁾ = +Q[h₁; G⁽¹⁾[h₁]/8πG] = Q[h₁; FT⁰]. The defect is the commutator of the gain with the gravitational force.
- **Static check** (Gaussian body of width R, hydrostatic in the record potential; out:19-21): ‖D‖/‖ρ∇U‖ = 0.101, 0.0137, 0.00128 at ℓ/R = 0.3, 0.1, 0.03, which is 1.1–1.4·(ℓ/R)².
- **No net force for an even gain (proved).** ∫ρ∂_i(K*f*ρ) = 0 by antisymmetry. The odd part of F_t gives R13-6's residual drag.
- **So R16-14:152 fails for geodesic matter, at order (ℓ/R)², (ωτ)².** The harmonic condition is then violated, and h₂ is not an Einstein metric.
- **The fix is Π (§3).** It is what R15-2 did for the noise (reconstruct from free data), now applied to the full O(G²) source.
- **Π's choice is unique only up to a conserved tensor of size O(G²)(ℓ/R)²**, localised in the body (reading). A static isotropic K changes only the O(G²) 1/r term, which is a mass renormalisation (proved), not β.

### 4.2 β and γ (proved; checked)

- **The LL field stress** of the static O(G) metric, from the exact identity (ll:7-9): (−g)t_LL⁰⁰ = −(7/8πG)|∇U|²; (−g)t_LL^{kk} = −(1/8πG)|∇U|²; (−g)t_LL^{xy} = (1/4πG)∂_xU∂_yU. Static t_H is O(U³), because h^{0j} = 0 and h^{jk} = O(U²) (proved).
- **Point mass at O(M²)** (ll:13-16):
  - h₂⁰⁰ = 7M²/r², h₂^{kk} = M²/r²;
  - g₀₀ = −√((1 − h^{kk})/(1 + h⁰⁰)) = −1 + 2M/r − 2M²/r²;
  - **β = 1**, identical to harmonic Schwarzschild.
- **E1 + N_c (N₁, Λ unfiltered).**
  - The record smears matter with F (static part e^{−k²ℓ²/2}). Outside the body, Λ equals the point-mass Λ to 3e-5 at r = 5ℓ and 2e-13 at r = 8ℓ (out:12-13).
  - With Π the exterior is a GR vacuum at O(G²), up to erfc tails. **β = 1 exactly in PPN form.**
  - γ = 1 at O(G) (`vR16-14:5`). E1's frame-tied non-PPN terms 6(ωτ)² are inherited unchanged (`vR16-14:5,11`).
- **Choice N_F** (Λ also filtered, R16-14's literal F·τ).
  - Extra term in g₀₀: 4ℓ²M²/r⁴, which is non-PPN (proved from (F−1)Λ = (ℓ²/2)∇²Λ + … and ∫(F−1)Λ = 0).
  - Checked: tail source to 0.1% at r = 100ℓ and 1000ℓ (out:3-5). dg₀₀·r⁴/ℓ² = 4.12 and 3.91 at r = 10ℓ and 30ℓ, against 4 (out:8-9).
  - The r ≥ 100ℓ potentials (out:10-11) are quadrature-limited and are not used.
  - Solar size: (ℓ/R_☉)² ≤ 5e-29.
- **Aside (checked, ll:17).**
  - A metric whose gothic variable is linear in records (Λ = 0) gives g₀₀ = −1 + 2M/r − 6M²/r², so β = 3. The perihelion factor (2 + 2γ − β)/3 = 1/3 gives 14.33″/cy against 42.98″/cy.
  - So Lemma L's conclusion does not depend on which variable is "linear": metric-linear gives β = 0, gothic-linear gives β = 3.
  - Recording this as an exclusion would need a referee.

### 4.3 Well-posedness, and "a functional of records plus P88" (proved; one estimate suggested)

- **Each order is a linear flat wave equation.** Its source is an explicit functional of records and lower orders. The retarded solution exists, is unique and is causal (comparator).
- **The products in Λ[h₁] are finite.**
  - The spatial gain is Gaussian.
  - f(0) = f′(0) = 0 (`vR15-2:9`), so K(0) = K′(0) = 0 for K = f⋆J₀. Then ḣ and ḧ are filtered noise with no white term (proved by K′(0) = f(0) = 0 and the referee's K′ formula, `vR15-2:13`).
- **Data.**
  - P76's B uses S^{0ν}(t₀) = (−g)J^{0ν} + Λ^{0ν}. Λ(t₀) is a function of the constraint-solved h(t₀), so no new record is needed.
  - The only free data at each order are homogeneous solutions of □. P88 zeroes the TT ones. The residual harmonic gauge modes must also be zeroed: a one-clause extension of P88 (reading).
  - **So the readout is a functional of records + P76 + P88** (with the extension). This confirms S23's interlock (`S23:262`) at O(G²).
- **Perturbative at t_H (suggested).** Harmonic-gauge noise variance ≲ R_max × Poisson value ≈ 2.8e35 × 8e-59 ≈ 2e-23 ≪ 1 (R15-2's ⟨φ²⟩_S ≤ 8e-59 is order-of-magnitude only, `vR15-2:13`).

## 5. Probe (b): CP of the composite map

- **Proved.** With a = 4 the matter–meter instrument is R13-6/R15-2's unchanged Gaussian instrument. Everything that N adds is one of two things:
  - classical processing of records into h: nonlinear in records, but no quantum operation;
  - the record-controlled feedback unitary exp(−i dt H_m[ψ; g[h_{<t}]]).
- R13-6's per-step decomposition (`R13-6:281-290`) applies verbatim: unitary, homodyne instrument, record-controlled unitary, partial trace. A record-controlled unitary is CP for any classical dependence, including the non-Gaussian h₂ ∝ ξ² in the feedback. So **CP holds for every finite rational network at Gaussian order in the matter–meter coupling.**
- The exact irrational limit inherits `vR15-2:15`.
- **Toy check** (out:50-55): a qubit under a weak σ_z measurement for 6 steps. The strength depends on records; the feedback angle depends nonlinearly on records (q ← q + r + 0.7rq²).
  - Choi eigenvalues 0.165, 0.191, 0.757, 0.887, all ≥ 0; trace-preservation error 2e-16.
  - Linearity defect 1e-16.
- **N̄ is excluded within CP (proved; checked).** N̄ feeds back t_LL of the mean metric ⟨h⟩_ρ, a function of the state. The map ρ ↦ Φ_{⟨h⟩_ρ}(ρ) is then not linear. In the toy, state-dependent feedback gives a linearity defect of 1.6e-2 (out:54).
- So **of R16-14's two completions, only realised-field N admits a CP map.** This sharpens `R16-14:161` and the referee's remark that the axioms do not by themselves forbid N̄ (`C5_R16-14_referee.md:16`). The exclusion rests on linearity of the quantum map, not on `AX:82-83`.

## 6. Probe (c): β, γ and the noise-fed corrections at O(G²)

- **β = γ = 1** (§4.2).
- **The noise-fed mean** (scalar ρ-noise, static, homogeneous; out:24-37).
  - Identity: ⟨U_nρ_n⟩ = 2|u₁| with |u₁| = ⟨|∇U_n|²⟩/(8πG) (checked: 2.000 in four realisations).
  - If the noise enters the O(G²) source as (1 + aU)ρ_n, then ⟨τ⁰⁰⟩ = (2a − 7)|u₁| and the active density is ⟨τ⁰⁰ + τ^{kk}⟩ = (2a − 8)|u₁|.
  - **The active density is invariant under a change of spatial gauge.** The exact static lapse equation D²N = 4πGNρ_H (identity checked, lapse:1-3) gives ⟨∇²N₂⟩/(4π) = 2(2 + a′)|u₁| with a′ = a − 6. Numerically this is −8.0000, −0.0000 and +4.0000|u₁| at a = 0, 4, 6, equal to 2a − 8 (out:34-36).
  - **The choices:**
    - **a = 4** keeps R13-6/R15-2's meter (which measures T) and forms τ = (−g)(J + t_LL) + t_H on the classical side. It gives **zero active density**. This is a reading; R16-14's "F·τ" (`R16-14:143-145`) does not say where the noise enters.
    - **a = 0** (the meter adaptively measures (−g)T, with noise added after) gives −8|u₁|.
    - **a = 6** (noise as static dust) gives +4|u₁|.
- **Against Mercury.**
  - |ρ_act| < 9.29e-15 kg/m³ (`vR16-14:11`).
  - At a = 0, Mercury fails for ℓ ≲ 3e-8 m (strict; ×1.38 at 3e-8 m) and near ℓ = 4e-10 m (τ_c ceiling; ×11.7) (out:59-66). These regions are already outside R15-2's premise-(iii) window.
  - At a = 4 there is no static scalar-noise contribution at this order.
- **The other noise-fed terms** (O(h_b h_n²) dressing, timing jitter) are as R16-14 §5.2-5.3, model-level (`vR16-14:11`). They are not recomputed.
- **Time-dependent S/V terms: not computed gauge-invariantly** (caveat 1).

## 7. Probe (d): is premise (iii) forced?

- **Qualitatively, yes.** CP requires the realised field (§5). Λ is quadratic in the realised h, and h contains the record noise. So the noise's field stress enters the O(G²) source with a nonzero mean (⟨Λ⁰⁰⟩ = −7|u₁|, out:27) (proved).
- **Quantitatively, no (checked, in scope H4).**
  - The local gravitating (active) density of the static scalar noise is (2a − 8)|u₁|. It is fixed by how the record noise is inserted (a), and **vanishes for the unchanged-meter reading of N (a = 4)**.
  - The LL energy density there is +|u₁|. Whether that counts against ρ_Λ in an expanding universe depends on an averaging definition and an FRW treatment, neither of which is built here.
  - A stationary noise with (ρ, p) = (|u₁|, −|u₁|/3) is not FRW-conserved at constant density. That is R17-11/R18-6 territory (suggested).
- **So the expectation that "R15-2's constraint-energy overshoot is live again" holds only for a ≠ 4 locally, or for the energy budget under the LL definition.** In the scope computed, it is a law choice, not a consequence.
- **Not covered:** the T_⊥ noise (anticorrelated at the least-decoherence split, `R15-2:125`), the V channel, the TT channel (expected to enter as Isaacson radiation, suggested), and time dependence.

## 8. Probe (e): prices (named, not adopted)

Carried: P65 (E1), P76, P88, P107, P-r15b. New in this item:
- **P-r18-7a (conserving projection Π).** One sentence: "The metric record's source is the causal conserving completion of the recorded total stress." Without it, N does not close at O(G²) (§4.1). *Axiom text:* the source/action gate (`AX:187`). Its freedom is an O(G²)(ℓ/R)² ambiguity.
- **P-r18-7b (gauge of the O(G²) readout).** One sentence: harmonic coordinates of the CMB frame. It conflicts with P-r15b's Poisson-gauge record of the S/V noise: either replace P-r15b at O(G²), or build the Poisson-gauge second-order law (not done). *Axiom text:* `AX:82-83` (the readout).
- **P-r18-7c (noise insertion weight).** One number, a. a = 4 (unchanged meter, classical densitisation) gives zero static active noise density; a = 0 (adaptive meter of (−g)T) gives −8|u₁|. *Axiom text:* `AX:82-83`, `AX:187`.
- **P88 extension.** The residual harmonic gauge modes' free data are also zero at t₀. This clause rides on P88 (`AX:92-94`, `AX:185-186`).
- **Not a price, a consequence:** N̄ is excluded by CP (§5), so the owner's Q2 option N̄ (`S23:647`) is not available inside a CP law.
- **Count:** E1 + N_c = P65 + P76 + P88 (+ clause) + P107, made concrete as N₁ realised-field with a = 4, plus P-r18-7a, P-r18-7b and P-r18-7c. That is three new stipulations: two sentences and one number.

## 9. Strong words checked

- **"Does not close" (§4.1).** For geodesic (minimally coupled) matter with a non-trivial gain, at order (ℓ/R)² and (ωτ)². Checked for one static profile. The formula is proved from the LL identity and Bianchi.
- **"β = 1 exactly in PPN form."** Static weak field at O(G²). The exterior is a GR vacuum up to erfc(r/√2ℓ) tails, and outside the support of K. E1's 6(ωτ)² terms remain (non-PPN).
- **"CP."** For finite rational meter networks, at Gaussian order in the matter–meter coupling. The exact irrational limit is conditional.
- **"N̄ excluded."** Within the requirement that the quantum dynamics be a linear CP map. This is a structural proof plus a toy, not a theorem about every conceivable mean-field law.
- **"Gauge-invariant active density."** Under O(G) homogeneous spatial coordinate changes, in static slicing. The time slicing and time-dependent noise are not covered.
- **"Zero at a = 4."** Static scalar ρ-noise only, at O(G·noise²).
- **The R(k) figures.** These are per-mode ratios of the secular harmonic-gauge energy to the Poisson-gauge analogue. The k-integrated effect on ⟨Λ⟩ is not computed.

## 10. What would decide it

1. **A referee of §4.1** (literal N does not close; the defect formula) and of §5 (N̄ is not CP).
2. **The O(G²) law in Poisson gauge** (second-order Poisson-gauge equations with Π), to remove caveat 1 and keep P-r15b. Alternatively, a gauge-invariant (Bardeen-type) second-order noise-fed computation including the time-dependent S/V noise.
3. **The noise-fed mean for the T_⊥ and V channels** at a = 4, and an FRW version with stationary noise, to settle the energy budget (with R18-6's bridge).
4. **Owner:** whether a = 4 (unchanged meter, classical densitisation), with zero static active noise mass, is the intended reading of P107.

**Sources (RECALLED):**
- Landau & Lifshitz, *Classical Theory of Fields* §96 (pseudotensor and identity);
- Poisson & Will 2014, *Gravity* ch. 6–7 (relaxed equations, t_H, harmonic gauge);
- Will 2014 (PPN; perihelion (2 + 2γ − β)/3);
- the harmonic-coordinate Schwarzschild metric;
- the static identity R₀₀ = N D²N;
- the retarded □² Green function;
- Gisin 1990 and Polchinski 1991 (nonlinear quantum dynamics);
- Matarrese, Mollerach & Bruni 1998 (second-order Poisson gauge; not used).

Via earlier referees: the Mercury active-density bound (`vR16-14:11`); |u₁| and I_F (`vR15-2:17`); GR perihelion 42.98″/cy (`vR16-14:13`).
