# C5 R15-6 report: can the lattice-time reader keep the CMC sector healthy? A sign theorem for g

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-12, 22:10Z to about 22:45Z. No repository file was edited.

**Scratch folder.** `S/` = `.../scratchpad/C5/R15-6/`. Scripts and outputs are in `S/scripts/`. Each runs in under a minute at `OMP_NUM_THREADS=2`.
- `r156_identity.py/.out`: the reader identity (sympy), checked numerically against R15-1's g on R14-5's own runs.
- `r156_mr.py/.out`: the memory reader MR on class H1, and four histories outside H1.
- `r156_bounds.py/.out`: what any size bound on g costs. Lemma L (collapse after drops), Lemma U (runaway after rises), and the oracle reader on rises.
- `r156_linear.py/.out`, `r156_linear_lp.py/.out`: linear fading-memory readers (the R15-4 class). It contains Theorem L's numeric check and an LP sign-feasibility scan.
- `r156_cpl.py/.out`, `r156_cpl_fit.py/.out`: DESI-like CPL histories with the oracle, Prony-2, MR and a family-matched reader FM.
- `r156_influence.py/.out`: the size of the instantaneous influence today, against stated bounds.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`); `TESTS.md:2302-2320` (the C5 method); the Λ entries `TESTS.md:4157-4188`, `:4317-4320`, `:4351-4363`, `:4417-4424`, `:4505-4517`, `:4621-4641`, `:4721-4729`, `:4876-4916`; R15-1 to R15-6 at `TESTS.md:4924-5035`; `agents/C5_R14-5_report.md` (`R145`); `agents/C5_R14-5_referee_verdict.md` (`vR14-5`); `agents/C5_R15-1_report.md` (`R151`); `SUMMARY.md:534-675` (§§21–25).
- The R15-1 scripts in `scratchpad/C5/R15-1/scripts`: `r151_quadratic`, `r151_reduce`, `r151_window`, `r151_homog_gsign` and `r151_signal`, with their outputs.
- The R15-1 referee verdict, which appeared during this run: `scratchpad/C5/ref_R15-1/REFEREE_VERDICT.md` (`vR15-1`). It is **CONFIRMED WITH CORRECTIONS, FAIL**: Lemma S and the exact ghost band g > 6H² are confirmed, and the tachyon thresholds are "frozen-background diagnostics" only (`vR15-1:5,11,19`).
- R15-4 worker scripts (still running, unrefereed): only the headers of `scratchpad/C5/R15-4/scripts/r154_reader.py:1-20`. Its reader is linear: y_j′ = E − β_j y_j, ρ̂ = Σ k_j y_j, with G(3) = G(4) = 1 imposed.

**Labels.** proved / checked (sympy or numerics this run) / suggested / reading / comparator. A comparator is **RECALLED** (nothing was fetched this run).

**Units and subtraction rule (named before the runs).**
- Units: homogeneous, κ = 1, u = ln a, 3H² = R (the reader's output, `R145:163`).
- ρ_nc is the true non-vacuum content. ρ_v is the w = −1 stress at each instant.
- e := R − ρ_nc is the reader error, so Λ̃ = κe homogeneously (`R145:24`).
- V := ρ_tot − R is the reader's inferred vacuum.
- α := Δ/ρ_nc is the relative size of a vacuum change, taken just before the change unless stated otherwise.
- Nothing else is subtracted.

---

## 0. Verdict against the FIXED readings (`TESTS.md:5031-5035`)

**Worker reading: PASS, scoped to the stated class H1 only. For the referee.**
- **The reader.** The memory reader MR (§4.3) is explicit, causal and regular, and it annihilates constants.
- **The class H1.** Homogeneous radiation plus conserved dust plus a w = −1 vacuum that never increases, with the latent heat going into radiation and a quiet start.
- **What is proved on H1.**
  - Λ̃ ≡ 0 at every instant.
  - g/H² = ρ_v′/ρ_nc ≤ 0, so g is never positive. That places it outside R15-1's ghost band, which is exact for g > 6H² (`vR15-1:11`), and in the region R15-1 sampled as tachyon-free.
- **The influence against stated bounds.**
  - Today g = 0 in H1. With lumpiness, g is about 1e-5 H₀² (suggested).
  - The local instantaneous acceleration is 5e-33·(|g|/H₀²) m/s² near the Sun, against an ephemeris bound of about 1e-14 m/s² (RECALLED).
  - During a transition, the time-integrated Hubble-scale response is at most about ¼·ln(1 + α) (checked).

**What PASS does not cover.**
- **H1 is a toy class.** It excludes:
  - mass thresholds such as e± annihilation, where MR leaves a permanent dust-like error of −24% in the test (checked);
  - latent heat going into non-radiation sectors (−15%);
  - DESI-like dark energy (MR −58%);
  - lumpy late times.
- **For the item's question "for all physically allowed histories", the evidence gives INCONCLUSIVE.**
- **It does not undo R15-1's refereed FAIL.** MR has g ≠ 0 during every absorbed drop, and Lemma C forces that (`vR14-5:18-25`). So Lemma S signalling is still present during transitions.

**Necessity results that limit every reader in R14-5's class (for the referee; FAIL-type in their stated classes):**

| # | Result | Class | Label |
|---|---|---|---|
| **I** | g/H² = V′(u)/R: the sign of g is the sign of the change in the reader's inferred vacuum | homogeneous, Lemma C bookkeeping | proved (sympy); checked |
| **B** | Every constant-annihilating reader is a functional of the enthalpy history h(u) = (ρ+p)_tot. That history is blind to any w = −1 stress at every instant | H-T (total conservation) | proved |
| **N** | NEC + Lemma C do **not** force the sign of g. A vacuum *rise* fed by radiation keeps the NEC and forces ∫(g/H²)R du = +Δ for every reader that is exact before and after | homogeneous | proved; checked (oracle g/H² up to +34) |
| **L** | Any reader with g ≥ −c₋H²: after a fast drop with α > c₋/4 into radiation, R → 0 (H → 0) in finite time | radiation after the drop | proved; checked (20/20 cases match) |
| **U** | Any reader with g ≤ c₊H², c₊ < 4: after a fast rise with α > c₊/4, the residual Λ̃ grows to dominate, as a w = c₊/3 − 1 fluid | radiation after the rise | proved; checked (16/16) |
| **T** | Tracking within η through a drop of width W forces sup\|g\|/H² ≥ [α − η(2+α)]/[(1+η)(1+α)W], up to O(W) dilution corrections in the denominator | homogeneous | proved (elementary) |
| **Theorem L** | No *linear* fading-memory reader that is exact on both dust and radiation keeps g ≤ 0 after every step drop into either sector. So the R15-4 reader class has g > 0 after fast drops. A sign theorem needs a nonlinear reader (MR's running minimum is one) | linear causal kernels with ∫\|K\|e^{4s} < ∞ | proved; checked |

**Answer to (c).** No. NEC and Lemma C do not force g's sign. For any reader that is exact on a class, sgn g = sgn of the change in the w = −1 stress *that the reader's content model leaves invisible*.
- For cooling into the true vacuum that change is downward, so g ≤ 0 (suggested; bag-model thermodynamics RECALLED).
- A field that freezes at nonzero potential, or radiation feeding the vacuum, is an upward change. It forces g > 0, and Lemma U applies.

---

## 1. In plain words

- **What g measures.** The number g is the rate at which the reader moves energy into or out of its "vacuum" bin, measured against the energy it counts as real content. If the reader decides there is *more* vacuum than a moment ago, g is positive (the unhealthy sign). If it decides there is *less*, g is negative (healthy, but it still signals instantly).
- **The sign is not set by energy conditions.** The null energy condition only says matter can't have negative pressure-plus-energy. It says nothing about whether energy flows into the vacuum or out of it. Cooling transitions move energy out of the vacuum, which is the healthy direction. A field that stops rolling at a nonzero potential moves energy into it.
- **A reader that never goes the wrong way.** For a universe of radiation and cold matter in which the vacuum only ever drops, a simple reader is exact at every instant. It keeps a running minimum of one number, the "cold-matter coefficient". Its g is never positive, and the leftover cosmological constant is exactly zero, even through very fast transitions. But it miscounts as soon as particles turn non-relativistic (as electrons and positrons do during BBN), or when dark energy evolves.
- **Linear readers can't do it.** Any reader that is a fixed weighted average of the past (the R15-4 design) and is exact for both matter and radiation must overshoot after a fast transition. That briefly makes g positive. The only way around this is a one-sided (nonlinear) memory.
- **You can't cap g both ways.** If a fast transition dumps more vacuum energy into radiation than about c/4 of the content, a reader limited to |g| ≤ cH² either lets the expansion stop (for drops) or lets its own error grow until it runs the universe (for rises). So either |g| must be allowed to be large during fast transitions, or those transitions must be excluded.
- **Today it doesn't matter.** Any g up to many times H₀² gives a near-instant extra pull of order 1e-33 m/s² near the Sun, far below what planetary tracking could see. On Hubble scales g/H₀² ≲ 0.05 is compatible with growth data (suggested).

---

## 2. Hypotheses and classes (stated before titles)

- **H-T.** Total stress is conserved and homogeneous, so ρ_tot′ = −3h with h := (ρ+p)_tot (`R145:99`, H-T; `vR14-5:7-19`).
- **H-read.** The zero mode is 3H² = κR, where R is a causal functional of the slice-averaged ρ̄_tot history that annihilates constants: R[ρ + C] = R[ρ] (`R145:101`; `TESTS.md:5028`).
- **Lemma C** (refereed, `vR14-5:7-25`): λ = E_nn and λ̇ = −gθ, with θ = 3H homogeneously.
- **H1** (class for MR):
  - content = radiation ρ_r plus dust ρ_m = m₀a⁻³ plus a w = −1 stress ρ_v(u);
  - ρ_v is non-increasing;
  - all latent heat q_lat = −ρ_v′ ≥ 0 goes into radiation;
  - ρ_tot ∈ C²;
  - some instant before the first change has q_lat = 0 (a quiet start).
- **Health thresholds used** (from R15-1, refereed with corrections):
  - ghost for g > 6H², exact for the canonical-scalar test (`vR15-1:11`; re-read in `r151_reduce.out`, A's denominator 4H²k² + a²χ̇²(6H² − g));
  - tachyon thresholds of about 1–5H², which are diagnostics only (`vR15-1:11`);
  - g ≤ 0 had no ghost and no tachyon in the sampled range g/H² ∈ [−1000, 0] (`R151:174`; `r151_window.out`).
- **Excluded:** inhomogeneous (lumpy) dynamics except the averaged-constraint term (§4.6); a Z³ construction; cubic order; the source-bridge choice (`AX:187`).

---

## 3. Prior art (each counted once)

1. **R14-5 and its verdict.** These supply:
   - Lemma C;
   - the homogeneous bookkeeping g = −2Ḣ − κ(ρ+p) (`R145:196`);
   - the Prony reader with near-singular Hankel points and H² < 0 (`vR14-5:41`);
   - lumpy Λ̃ = ½⟨R⟩ − ½⟨σ²⟩ (`R145:257`; `vR14-5:44`).
2. **R15-1 and its verdict.** These supply:
   - Lemma S (`R151:122-147`; confirmed, `vR15-1:5`);
   - g = κρ̇_v/(3H) for an exact reader (`R151:143`);
   - Prony g/H² up to +1e3 (`R151:179`);
   - the reader condition P-r15b, g < g_crit (`R151:254`).

   This item answers P-r15b.
3. **R12-2 / R13-3.** The Prony P-T rule and the observation that "a rule that reads only time changes of energy" makes a true Λ invisible (`SUMMARY.md:664`; `TESTS.md:4509-4517, 4721-4729`). The S6 point, that acceleration needs w ≠ −1 dark energy, is carried (`R145:340`).
4. **R15-4 (worker, running).** The linear reader class (`r154_reader.py:1-20`, unrefereed). Theorem L applies to it.
5. **Comparators (RECALLED).**
   - Bag-model QCD thermodynamics (the false vacuum lies above the true vacuum for cooling transitions).
   - The SM electroweak and QCD transitions are crossovers.
   - Planetary-ephemeris limits on an anomalous radial acceleration of about 1e-14 m/s²; LLR limits of about 1e-13 to 1e-14 m/s².
   - The PBH collapse threshold δ_c ≈ 0.4–0.5.
6. **Repository grep.** I grepped "reader", "sign of g" and "running min" in `P/agents`. The only hits are R12-2 to R15-1 reader text (no separate sign theorem). No repository treatment of a one-sided (ratchet) reader was found.

---

## 4. Results

### 4.1 Lemma I (identity) and Lemma B (blindness)

**Lemma I (proved; checked).** Homogeneously, with 3H² = R, λ = 3H² − ρ_tot = −V. Lemma C then gives λ̇ = −3Hg, so

  **g/H² = V′(u)/R = −(R′ + 3h)/R.**

- `r156_identity.out:1-2`: sympy gives g_formula − V′/3 ≡ 0.
- On R14-5's five step runs with the Prony-2 reader, R15-1's finite-difference g agrees with V′/3 to a median of 5e-4 to 3e-3 on smooth samples (`r156_identity.out:3-7`).
- **Corollary (proved).** For any interval, ∫(g/H²)R du = V(u₂) − V(u₁) = Δρ_v − (e₂ − e₁).

**Lemma B (proved).**
- Suppose R[ρ + C] = R[ρ] for all constants C. Take C = ρ(u). Then R depends only on the differences ρ(u′) − ρ(u) = 3∫_{u′}^{u} h, i.e. on the h-history.
- Under H-T, h = (ρ+p)_tot gets no contribution from any w = −1 stress at any instant, constant or not.
- So every reader in R14-5's class sees a vacuum change only through the latent heat it injects into h.
- **Consequence.** A supercooled false vacuum (w = −1, constant until it converts) is invisible to every reader in the class until it converts. Its removal must then be absorbed, which forces g ≠ 0 (Lemma C).

### 4.2 (c) The sign is not forced by the NEC (Lemma N)

**Exact reader (proved).** If R = ρ_nc on a class, then V = ρ_v and g/H² = ρ_v′/ρ_nc. This agrees with `R151:143`. So sgn g = sgn ρ̇_v: drops give g ≤ 0, rises give g ≥ 0.

**Counterexample to "NEC forces the sign" (proved; checked).**
- **The history.** Radiation feeds the vacuum: q′ = −4q − |D|s′(u), with ρ_v rising by |D|.
- **The NEC holds.** h = (4/3)q > 0 throughout, with min q·e^{4u} = 0.9, 0.7 and 0.5 for α = 0.1, 0.3 and 0.5 at W = 0.01 (`r156_bounds.out`, oracle section).
- **Every reader that is exact before and after** has ∫(g/H²)R du = +Δ > 0, so g > 0 somewhere (Corollary). The checked integrals equal α (+0.1000, +0.3000, +0.5000).
- **The oracle's peak** g/H² is +5.3, +17.8 and +34.2 at W = 0.01, which is above the exact ghost line 6 for α ≥ 0.3.

**Where drops come from (suggested).**
- In a cooling first-order transition, the false phase has higher zero-temperature vacuum energy (B_f > B_t, bag-model thermodynamics, RECALLED), so the w = −1 stress drops.
- Rises in the reader's accounting arise when a component it counts as content freezes into a constant, such as a field stopping at V ≠ 0, or from explicit energy flow into a w = −1 stress.
- Whether such histories are physical is a reading. The source bridge `AX:187` decides what a "vacuum stress" may exchange (`vR15-1:13`, Lemma V).

**Answer to (c).** Not forced. The sign is the sign of the invisible w = −1 stress's change (exact readers), plus reader error (inexact ones).

### 4.3 (a) An explicit reader with a proved sign bound: MR on H1 (Theorem M)

**Rule.**
- B(u) := 4h + h′.
- m̂(u) := min_{u′≤u} e^{3u′}B(u′), a running minimum over the past.
- R := ¾h + ¼m̂e^{−3u}.

**Properties.** It uses only h and h′, so it annihilates constants (Lemma B). It is causal (a minimum over the past) and real. It needs ρ_tot ∈ C².

**Theorem M (proved).** On H1:
- h = (4ρ_r + 3ρ_m)/3 and h′ = (4(−4ρ_r + q_lat) − 9ρ_m)/3, so e^{3u}B = m₀ + (4/3)q_lat·e^{3u} ≥ m₀, with equality wherever q_lat = 0.
- So m̂ = m₀ exactly after the quiet start, R = ρ_r + ρ_m = ρ_nc, Λ̃ ≡ 0, V = ρ_v, and **g/H² = ρ_v′/ρ_nc ≤ 0 at every instant**, for any speed or size of drop. ∎

**Checked** (`r156_mr.out:1-41`), on R14-5's five step histories plus three harder ones (W = 0.005; α_before ≈ 4.8 at W = 0.05; α_before ≈ 48 at W = 0.01):
- max|ε| = 1.5e-14 to 1.9e-8 (integration precision);
- MR g equals the oracle −ρ_v′/ρ_nc;
- min g/H² ranges from −0.035 to −152.

| Residual positive g | Cause | Lines |
|---|---|---|
| ≤ +1.7e-2 | round-off in V′ when R/V ≈ 1e-13 at late u | `r156_mr.out:19` |
| ≤ +2e-6 | as above | elsewhere |

Compare the Prony-2 reader on the same histories: g/H² up to +4e2 to +2.2e3 (`r156_identity.out:3-7`; `R151:179`).

**Outside H1 (checked, `r156_mr.out:42-62`):**

| History | MR outcome |
|---|---|
| 30% of latent heat to dust | permanent dust-like error ε = −14.8%; g ≤ 0 still |
| A species going non-relativistic (w: 1/3 → 0), no vacuum change | permanent ε = −24.2%; g/H² in [−0.97, +0.02] |
| The same plus a drop | max g/H² = +0.17 |
| A vacuum rise | MR breaks: R < 0, g/H² up to +739 |

So MR is exact only on H1. It is a toy class: the real radiation era contains e± annihilation during BBN.

**Generalization (proved conditional on exactness; adequacy suggested).** For any reader exact on a class C, Lemma I gives g/H² = (ρ_v^C)′/ρ_nc^C, where ρ_v^C is the part C's content model leaves invisible.
- Example: a barotropic equilibrium content with a supplied EoS. The reader R = ρ_EoS(T(h)) − ρ_EoS(0) inverts h = Ts(T), which is monotone because d(Ts)/dT = s + c_V > 0. It is exact, V is constant, and so **g ≡ 0**.
- So through equilibrium crossovers (the SM EW and QCD transitions are crossovers, RECALLED) and equilibrium mass thresholds, such a reader keeps the CMC sector in Lemma C's case (A): no absorption, no Lemma S signalling.
- **The price (P-EoS):** the creation law carries the content's equation of state. Decoupled species need a shape memory like MR's.
- This was not run.

### 4.4 Theorem L: linear readers have no sign theorem (proved; checked)

**Class.** R(u) = ∫₀^∞ K(s)E(u−s)ds, with E = 3h, ∫|K|e^{4s} < ∞, and G(x) := x∫K e^{xs}ds. R15-4's reader is this class with K = Σk_j e^{−β_j s} and G(3) = G(4) = 1 imposed (`r154_reader.py:1-12`).

**Step response (re-derived).** After a step release Δ into a sector of rate x, with the reader exact before:
- e(τ) = −xΔ∫_τ^∞K(s)e^{x(s−τ)}ds;
- **e′ = xΔ·P_x(τ)**, with P_x := K(τ) + x∫_τ^∞K(s)e^{x(s−τ)}ds;
- g/H² = −e′/R. So g ≤ 0 for all τ ⟺ P_x ≥ 0.

**Identity (proved).** ∫₀^∞P₄(τ)e^{3τ}dτ = ∫₀^∞P₃(τ)e^{4τ}dτ = G(4) − G(3). Checked to 1e-15 (`r156_linear_lp.out`, last lines).

**Theorem L.**
- If G(3) = G(4) = 1 and P₄ ≥ 0, the identity forces P₄ = 0 a.e. Then e is constant and equal to e(0⁺) = −Δ ≠ 0.
- But e → 0, because G(4) = 1 and ∫|K|e^{4s} < ∞. That is a contradiction. The same argument works for P₃.
- So **every linear reader exact on dust and radiation has g > 0 after some step drop into either sector.** For releases of finite width it does so whenever they are fast enough (continuity in W). ∎

**Lemma K (proved).** If all k_j ≥ 0, G is strictly increasing, so G(3) = G(4) is impossible: exact linear readers need weights of both signs. For two registers the slow weight is forced negative, which gives a late overshoot.

**Sizes (checked, `r156_linear.out`).**
- 2-register exact designs: after an α = 1 drop, max g/H² ≈ 1.1 to 17.7 (it scales as α/(1+α)).
- LP scan over 3–12 registers: no sign-safe design; the best margin is −1.5 to −4.9 (`r156_linear_lp.out:1-12`). The 2-register LP returned "infeasible", a numerical artefact of e^{−βτ} underflow; the 2-register case is covered by `r156_linear.out`.
- **So:** R15-4's reader cannot meet "g ≤ 0". At best it meets "g ≤ cH²" for small enough α, depending on the design. MR's running minimum is the nonlinearity that escapes Theorem L on H1.

### 4.5 What a size bound on g costs (Lemmas L, U, T)

From Lemma I, e′ = ρ_v′ − (g/H²)R holds for **any** reader. With radiation after the change (ρ_nc′ = −4ρ_nc), x := e/ρ_nc and y := R/ρ_nc = 1 + x:

**Lemma L (proved).**
- If g ≥ −c₋H², then y′ ≤ −4 + (4 + c₋)y. If y < 4/(4 + c₋), R reaches 0 in finite u (H → 0, expansion stops).
- After a fast drop, y ≈ 1/(1+α), so collapse occurs iff c₋ < 4α.
- **Checked:** 20/20 cases of the best capped reader (oracle estimator) follow the prediction (`r156_bounds.out:1-21`).

**Lemma U (proved).**
- If g ≤ c₊H² with c₊ < 4, then x′ ≥ −c₊ + (4 − c₊)x. If x > c₊/(4 − c₊), x grows like e^{(4−c₊)u}: the residual Λ̃ decays only as a^{−c₊} and comes to dominate as a w = c₊/3 − 1 fluid.
- After a fast rise, x ≈ α/(1−α), so runaway occurs iff α > c₊/4.
- **Checked:** 16/16 cases (`r156_bounds.out:22-38`).
- **Slower rises.** At W = 0.3, α = 0.3 is absorbed for c₊ = 1, while α = 0.5 runs away even for c₊ = 2 (`r156_bounds.out:39-43`).

**Lemma T (proved, elementary).**
- If |e| ≤ ηρ_nc at the ends of a drop window of width W, the Corollary gives sup|g|/H² ≥ [α − η(2+α)]/[(1+η)(1+α)W]. This uses ρ_nc after ≈ (1+α)ρ_nc before; dilution over W adds O(W) corrections to the denominator.
- **Checked against MR** (exact, η = 0): the tanh width W = 0.005 (window ≈ 2W) and α_before = 0.29 give peak |g|/H² = 25, against the bound's 22 (`r156_mr.out:29`).

**Consequence for (b).** A uniform size bound |g| ≤ cH² over all drop histories is impossible. Fast drops with α > c/4 force either collapse (L) or loss of tracking. A uniform upper bound g ≤ c₊H² fails on fast rises with α > c₊/4 (U).
- With c₊ = 1 (no tachyon in any sampled background, diagnostic) the critical rise is α = 0.25.
- With c₊ = 6 (the exact ghost line) Lemma U imposes no runaway constraint, since c₊ ≥ 4.

### 4.6 DESI-like w and lumpy late times

**DESI-like history** (matter + CPL with w₀ = −0.75, w_a = −0.86 + any constant vacuum; the true vacuum is constant, so any g is reader error). Results checked in `r156_cpl.out` and `r156_cpl_fit.out`:

| Reader | g/H² (0.1 < a < 1) | Tracking | Comment |
|---|---|---|---|
| Oracle | 0 exactly | exact | — |
| Prony-2 (R14-5's) | [−2.8e3, +2.8e3] | ε up to 7.6e2; 116 complex-node samples | wild |
| MR | [−2.2, +0.06] | ε = −58% today | misses the dark energy: it sees only (3/4)(1+w)ρ_DE |
| Family-matched FM (4-parameter local fit of dust + CPL to derivatives d₁..d₄) | \|g\|/H² ≤ 1e-7 | exact on its own family | — |
| FM with unmodelled radiation Ω_r = 9e-5 | up to +4.8e6 early; −9e-4 today | — | fragile |

- FM annihilates constants and is causal.
- **Reading.** Exactness on a supplied family gives g ≡ 0 (Lemma I). Robustness to unmodelled content is unproved for every reader tested.

**Lumpy (suggested).**
- Averaging the CMC Hamiltonian constraint (`R145:257`) adds B := ½⟨R⁽³⁾⟩ − ½⟨σ²⟩. Lemma I becomes g/H² = V′/R − B′/(κR).
- The B′ term is reader-independent (the reader sees only ρ̄_tot). Its size is about 1e-5 at late times (magnitude RECALLED via `R145:59`, `R151:141`); its sign is not determined here.
- It is far below every health threshold.

### 4.7 (b) The size of the influence against stated bounds

**Local** (suggested; quasi-static limit).
- Here δp_E = −gδN (`R145:168`) and δN = Φ_N/c² in halos (`R145:216-220`, conditional). With ∇²Φ_x = (3/2)δp_E, a point mass gives Φ_x = (¾)g(GM/c²)r, set instantaneously on the slice (Yukawa-cut at about 0.8c/H₀).
- So |a_x| = (¾)|g|GM/c² (`r156_influence.out`). In units of |g|/H₀²:
  - Sun: 5.3e-33 m/s²;
  - Earth (LLR): 1.6e-38 m/s²;
  - double pulsar: 1.4e-32 m/s².
- Against an ephemeris limit of about 1e-14 m/s² and an LLR limit of about 1e-13 m/s² (RECALLED), these allow |g| < 1.9e18 H₀² and < 6e24 H₀². **Local tests do not constrain g**; the health thresholds bind first.

**Hubble scale.**
- The Lemma S fraction today is (3/2)(g/H₀²)/(k² + 1.35) (`r156_influence.out`, last block).
- **Stated bound:** growth/ISW consistency with GR at a few per cent on k ~ 1–10 H₀/c (RECALLED). That needs |g| ≲ 0.05 H₀² today (suggested; R14-5's growth form with the referee's ġ term, `vR14-5:72-80`).
- Exact readers (H1, FM on its family) give 0 there. The lumpy term gives about 1e-5.

**During transitions** (checked integral; suggested bound).
- The time-integrated k → 0 response is ∫(3/2)|g|/Q̄ du (`r156_mr.out:6-41`): 0.002–0.21 for α_before ≤ 0.6, 0.44 for α_before ≈ 4.8, 0.97 for α_before ≈ 48. These are close to ¼·ln(1+α).
- It acts on modes near the horizon at T_c. For SM-sized α ≲ 0.3, horizon-mode amplitudes change by ≲ 10%, far from the PBH threshold δ_c ≈ 0.45 with primordial δ ~ 5e-5 (comparator RECALLED; suggested).
- This is a size statement only. R15-1's FAIL on (a) stands, because signalling exists whenever g ≠ 0 (`vR15-1:17`).

---

## 5. Prices (named, none adopted)

| # | Price | Axiom text touched | Status |
|---|---|---|---|
| **P-r156a** | **One-sided memory reader** (MR): the creation law keeps a running minimum of e^{3u}(4h + h′), with a content model of radiation plus conserved dust. It buys g ≤ 0 and Λ̃ ≡ 0 on H1 | `AX:57` (a global reader, as P-r13b); `AX:184-187` (formation rules, source/action) | proved on H1; toy class |
| P-EoS | The creation law carries the content's equation of state (or per-species shapes). It buys g ≡ 0 on equilibrium/supplied-family histories | `AX:116-130` (no dynamics supplied); `AX:187` | suggested (conditional proof) |
| P-r15b (R15-1) | g < g_crit. **Answered on H1** (g ≤ 0). **Impossible for linear readers exact on dust and radiation** (Theorem L). Impossible uniformly over fast rises with α > c₊/4 (Lemma U) | `AX:186-187` | refined |
| P-r156b | **Fast-transition exclusion or large \|g\|.** The model must either forbid fast vacuum changes with α > c/4, or accept \|g\|/H² ~ α/W during them, with Lemma S signalling of that strength | `AX:186` | new, named |

---

## 6. Notes for the referee

**Items to check:**
1. **Lemma I.** λ = −V uses 3H² = R and E_nn = λ. The Corollary.
2. **Lemma B.** That "annihilates constants" ⇒ "a functional of the h-history" under H-T.
3. **Theorem M.** The B algebra (B = ρ_m + (4/3)q_lat) and the quiet-start condition.
4. **Theorem L.**
   - The step response for general K.
   - The identity ∫P₄e^{3τ} = G(4) − G(3).
   - The contradiction (e → 0).
   - The continuity step from steps to fast smooth releases.
   - Whether R15-4's final reader is in the class (only its header was read).
5. **Lemmas L and U.** The comparison ODEs, and the fast-change initial values y ≈ 1/(1+α) and x ≈ α/(1−α).
6. **§4.7.** The quasi-static Φ_x (uses δN = Φ_N, conditional), and the RECALLED bounds.

**Strong-word check:**
- "Exact" (MR): on H1, to integration precision.
- "Never positive": on H1, analytic. The numeric +1.7e-2 is round-off.
- "No linear reader": in the stated kernel class, for step releases, or fast enough smooth releases.
- "Impossible" (uniform size bound): for histories containing fast changes with α > c/4. Their physical status is a reading.
- "Local tests do not constrain": in the quasi-static Newtonian limit.
- "PASS": class H1 only.

**What would change the picture:**
- a nonlinear reader that is exact (or one-sided) on radiation + dust + mass thresholds (a shape memory) and on a dark-energy family;
- R15-4's final linear design, checked against Theorem L's overshoot size;
- the source bridge deciding whether vacuum rises are physical;
- an inhomogeneous CMC run for the B′ term's sign.

## 7. Files

- Report: `S/R15-6_report.md`.
- Scripts and outputs: `S/scripts/r156_identity`, `r156_mr`, `r156_bounds`, `r156_linear`, `r156_linear_lp`, `r156_cpl`, `r156_cpl_fit`, `r156_influence` (each `.py` with its `.out`).
