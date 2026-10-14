# C5 F4 report: gauge-path families for the SF-strained root Dirac hops

- **Worker:** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13, 13:13Z to 14:20Z. No repository file was edited. Nothing was downloaded. Every run used OMP_NUM_THREADS=2, ran one at a time, and stayed under 0.75 GB resident (peak seen 723 MB; checked with `ps`; z-slab chunks of 2e5 points). No process of mine is still running.
- **Item:** `TESTS:9261-9280`. FIXED readings at `:9276-9279`; expectation at `:9280`.
- **Paths.**
  - `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
  - `rX` / `vX` = `P/agents/C5_X_report.md` / `..._referee_verdict.md`. `rF1` = `P/agents/C5_F1_report.md` (worker; referee running).
  - `S/` = `scratchpad/C5/F4/`. Scripts in `S/scripts/`, outputs `S/*.out`, raw integrals `S/raw_*.json`. `f1_lib.py` is F1's library copied unmodified from `P/scripts/C5/F1/`; `S/arch/` holds unmodified copies of `dirac.py`, `sublum.py`, `zz.py`, `dfam.py` (from `P/scripts/C5/R18-5`) and `r1934_lib.py` (from `P/scripts/C5/R19-34`).
- **Labels.** proved (complete short argument, unrefereed) / checked (numerics run here) / suggested / reading / comparator. RECALLED = from memory.
- **Read.** `AX` in full; `TESTS:9146-9280` (C5 follow-up: F1, F2, F3, F4); `rF1` in full; `P/scripts/C5/F1/*.py` and `.out`; `rR19-34` in full and `vR19-34`; `rR19-31:1-70` and `vR19-31`; `PRICE_NOTE:18-26,670-690`.

## 0. Plain words, and the reading

**The question.** F1's strained Dirac operator hops diagonally, so every hop needs a gauge path. F1 averaged the six axis-ordered staircases ("Psym") and got an additive-mass E_g strain Hessian of +2.424e-2 e² (SF units). Do other path families change it?

**Answer: yes, by a few percent, upward; no genuine path average reaches zero (checked).**
- **Why it can change (proved).** Two path families differ by closed loops, so they differ only in how the fermion couples to the photon's field strength (Pauli-type and F² terms). At zero external momentum the photon inside the loop still carries the loop momentum, so those couplings contribute. Nothing forces them to cancel.
- **Where it starts (proved; checked).** At t = 0 the root's Dirac operator hops only along axes, and every family routes an axis hop along its axis. So all families are the same law at t = 0. The laws differ from O(t); the even quantity δm differs from O(t²).
- **The numbers (checked; the differences from Psym are converged to ≤ 6e-8 for J, S2, S4, S6 and to a few e-6 for S3 and S8-S32).** Hessian, R18-9 root, SF units:

  | family | local law? | Hessian | change from Psym |
  |---|---|---|---|
  | **P** = Psym (F1) | yes | +2.4240e-2 | — |
  | **J**: same six paths, but the hop phase is their averaged line integral (on unit-cube hops this is the straight line through the plaquette or cube centre, with the link field interpolated multilinearly) | yes | +2.4329e-2 | **+0.37%** |
  | **S_M**: M-round staircases, M = 2 … 32 | no (O(t) jump at the zone face) | +2.495e-2 … +2.590e-2 | +2.9% … +6.9% |
  | **SL**: the straight Peierls segment (= S_M as M → ∞) | no | ≈ +2.591e-2 | **+6.9%** |

  The 0⁺ root shows the same pattern (J +0.42%, S2 +3.1%, S4 +4.9%).
- **Where the shift lives.** 98-111% of each shift is in the two-photon (seagull/tadpole) term. F1's single-ordering probe could not see that, because every axis ordering has the same seagull; that is why its 4e-6 spread understated the path freedom.
- **Can it reach zero?** Not with any average of paths computed here: those are convex combinations, and every computed family lies between +2.42e-2 and +2.59e-2. A zero exists only for **signed** mixtures far outside the convex range: (1 − λ)·P + λ·J at λ* ≈ −273 (local), or (1 − λ)·P + λ·SL at λ* ≈ −13.5 (non-local). That is a tuned number, so it is priced (P-F4a below) and is not viable: like R19-34's κ*, it must hold to about 6e-9 to pass F2's Earth-crossing row.
- **What it means for F1.** F1's sizes scale linearly with the Hessian, so the Earth-crossing exceedance moves from 1.6e8 to between 1.6e8 and 1.7e8. F1's SF-HAZARD reading stands in every family. P-R19-34a (strain-covariant critical mass) removes the channel in every family, because it does not refer to the coupling's path.

**Reading (worker): PATH-SHIFTS.** Range: +0.37% (local J) to +6.9% (non-local SL) above Psym; all families computed are nonzero and the same sign. A zero is reachable only by a tuned signed mixture, priced as P-F4a and not viable. PATH-INVARIANT fails literally: the closest family (J) differs by 3.7e-3 relative, against the 1e-6 line.

## 1. Class, hypotheses, and the families (stated before any title)

**Arena (F1's, unchanged).** Z³ × ℝ, one loop, U(1), Euclidean, external P = 0, critical mass fixed at t = 0 (propagator m = 0), Feynman gauge, per e². E_g strain in SF units t (v = (t/2)diag(1,−1,0)·p; Hess_h = 4·Hess_t). Law: F1's B1 branch, D_t(k) = D(Φ^F_t(k)) on the R18-9 root D1(0.909103708, 0.555604226) (and the 0⁺ root D1(0.915438682, 0.568280847)), photon Gph(2.9435) with its own separable flow (`rF1:113-129`; `f1_lib.py:1-19`). Only the gauge path of each hop is varied.

**What a path family is here.** For every hop n of D_t a unit 1-chain from 0 to n (a probability measure μ_n over paths γ from 0 to n), cubic-covariant and reversal-symmetric (hermitian). The coupling of the hop is either
- **W-type:** the average of the Wilson lines, U_n = E_μ[exp(ie∫_γ A)] (F1's Psym is of this type), or
- **J-type:** the Wilson line of the mean current, U_n = exp(ie∫J̄_n·A), J̄_n = E_μ[J_γ] (unitary).
The photon is F1's generalized field: gauge transformation a_j(q) → a_j(q) + d_j(q)χ(q). A unit lattice edge from m along j carries e^{iq·m}(e^{iq_j}−1)/d_j(q); a straight segment from a to b carries (q_j/d_j(q))(b−a)_j∫₀¹e^{iq·(a+s(b−a))}ds, the line integral of the band-limited interpolation of the field. Both telescope, so every family satisfies the Ward identity Σ_j d_jV_j(0,q) = D_t(q) − D_t(0) (proved; checked 6.7e-16 at t = 0.3, `f4_validate.out:8`).

**Families computed** (`f4_lib.py:1-30`, momentum forms proved there and in §3.1):

| family | paths | type | local? | closed momentum form |
|---|---|---|---|---|
| **P** (F1's Psym) | the 6 axis-ordered staircases (one leg per axis), uniform | W | yes | corners of the box [0,q] (`rF1:124-127`) |
| **J** (Psym-J, plaquette/staple-average current) | the same 6 paths | J | yes | same vertex as P; seagull from the box corners with weights π = (10, 8, 8, 10)/36 |
| **S_M** (M-round staircase), M = 2, 3, 4, 6, 8, 16, 32 | each ordering σ repeated M times with legs n_j/M; uniform over σ | W | **no** for M ≥ 2 (fractional legs use the band-limited field) | corners P(r,S) = (rq + q_S)/M |
| **SL** (straight Peierls segment) | the straight segment 0 → n | single path | **no** (band-limited field) | V_j = (q_j/d_j)∫₀¹∂_jD_t(sq)ds; SL = lim_{M→∞} S_M |
| **mixtures** | signed W-combinations (1−λ)U_A + λU_B | W | as A, B | bilinear in λ |

- **Why these.** Within one-leg-per-axis paths, P is the only cubic hermitian W-average (`rF1:128`, proved there). Any other lattice-local family needs legs split at n-dependent integer points (Bresenham, all minimal paths, staples), which has no closed momentum form; those were not computed (§6). J is the local alternative with a closed form: the same six paths, but the hop phase is the averaged current. For the elementary plaquette hop (1,1,0) it is the straight diagonal through the plaquette centre with the link field bilinearly interpolated (proved by direct integration: ∫₀¹[(1−s)a_x(0) + s a_x(e_y)]ds = ½[a_x(0) + a_x(e_y)]); the same holds on every unit-cube hop (Lemma 4). So J is the local "via plaquette centres" family on those hops. S_M and SL realize the straight Peierls line; the band-limited interpolation is the only closed form I found, and it makes them non-local at O(t) (§3.1, Lemma 4).
- **Not varied:** axis hops. Every family routes an axis hop along its own axis, so all families coincide at t = 0 (Lemma 2). Families that also smear axis hops (fat links, APE staples) change R19-34's unstrained law itself; they are outside F4's question and not computed.

**Formula (F1's, unchanged in form).** δm/e² = base + Tad[s] + E[a,a], with base = ⟨M/(2EΩ(E+Ω))⟩, Tad[s] = ⟨Σ_j N^s_j/d_j²/(2Ω)⟩ (N^s_j the M-part of the diagonal seagull of family s), and the symmetric bilinear E[a,b] = ⟨Σ_j[(a_a·a_b − b_ab_b)M − b_a(a_b·c) − b_b(a_a·c)]/(2EΩ(E+Ω))⟩ for vertices V_j = iγ·a_j + b_j (`f1_lib.py:17-18,168-178`; `f4_lib.py:26-28`). M = 1 reproduces F1's `dm_sf` to 7e-18 (`f4_validate.out:2,5`).

**Hessian.** dm(−t) = dm(t) for every cubic family (the C₂ rotation about [110] maps each family to itself; proved as in `rF1:147`), so Hess = 2[dm(d) − dm(0)]/d², Richardson over d and 2d (d = 0.003; d = 0.0015 with nrk = 4 as a check). Quadrature: F1/R19-34 composite Gauss–Legendre on [0,π]³, optionally with extra panel breaks where a staircase corner component rq_l/M crosses the Dirac box edges ("fb").

**Excluded:** two loops; non-abelian vertices beyond C_F; T₂g; lattice-local families without a closed form (all-minimal-paths, Bresenham, multilinear-interpolated straight lines beyond the unit cube, staple-smeared off-axis hops); fat links on axis hops.

## 2. Prior art (counted once)

- **F1** (`rF1`, worker; referee running): the SF-strained law, Psym, its uniqueness among axis-ordered W-averages, B1 = +2.42401e-2 (344 nodes), the single-ordering sensitivity probe (+2.42359e-2 to +2.42423e-2, `rF1:204`), and the two freedoms left uncomputed (`rF1:135-136`). New here: families outside the axis-ordered class, the closed momentum forms of S_M and SL, and their Hessians.
- **R19-34 + vR19-34:** the divided-difference (generalized-link) convention for axis legs (`r1934_lib.py:7-9`), the t = 0 law, κ* as a tuned zero and its pricing as P-R19-34b ("needs 2e-16 precision", `rR19-34:126-127,181`).
- **R19-31 + vR19-31:** the channel and t = −2h.
- **Comparators (RECALLED, no numbers quoted):** in lattice QCD the one-loop critical mass of Wilson fermions depends on the clover coefficient c_SW (a σ·F coupling) and is strongly reduced by link smearing; both are changes of the field-strength coupling at fixed gauge covariance, which is what a change of path family is.

## 3. Results

### 3.1 (a) Which part is path-dependent (proved, short and unrefereed; inputs checked)

**Lemma 1 (a change of family is a field-strength coupling).**
- Two families A, B give, for every hop n, unit 1-chains from 0 to n. Their mean currents differ by a closed chain, so Σ_j d_j(q)ΔJ̄^n_j(q) = 0. In three components with d ≠ 0 this means ΔJ̄^n = d × u^n for some u^n, and the coupling difference Σ_j ΔJ̄_j a_j = u·(d × a) involves only the generalized field strength f_jk = d_j a_k − d_k a_j.
- So the one-photon vertex difference ΔV_j(0,q) = Σ_n K_t(n)ΔJ̄^n_j(q) is a field-strength (Pauli-type) coupling.
- **Seagull.** The W-type diagonal seagull is −½Σ_nK(n)E_μ[Ĵ_j(q)Ĵ_j(−q)] = −½Σ_nK(n)[J̄_j(q)J̄_j(−q) + Cov_μ(Ĵ_j(q), Ĵ_j(−q))]; the J-type keeps only the first term. Path fluctuations Ĵ^γ − J̄ are closed chains, hence transverse. So every family difference of the seagull carries at least one transverse (f-type) factor: A·f and f·f terms.
- **Consequence 1 (gauge parameter, proved).** A longitudinal photon (a ∝ dχ) annihilates every transverse factor. F1's ξ-independence argument (`rF1:185-190`) uses only the one-photon Ward identity and the longitudinal two-photon contraction, both family-independent. So δm(P = 0) is ξ-independent in every family, and the path dependence below is a property of the law, not of the gauge.
- **Consequence 2 (where it lives).** At P = 0 the external momentum is zero but the loop photon carries the loop momentum q, and in Feynman gauge its transverse polarizations have f(q) ≠ 0. Nothing in the P = 0 kinematics removes the f-couplings. This is the argument for PATH-SHIFTS; it is not a no-go, and the values are checked in §3.2.

**Lemma 2 (all families coincide at t = 0).** D_0 is separable, so K_0(n) = 0 off the axes. Every family routes an axis hop along its axis (staircases degenerate to one leg; the segment is the axis). So the laws are identical at t = 0. Checked: δm(0) equal in every family to all printed digits on every grid (`f4_validate.out:2-4`; `f4_A120.out:5-10`).

**Lemma 3 (order in t).** The off-axis part of K_t is O(t) (the Dirac flow is non-separable at first order through M in p_j = ss′ + MW′, `f1_lib.py:5`). So ΔV = O(t) and Δseagull = O(t). Each family is cubic, so dm is even in t, and the O(t) cross terms vanish. The Hessian difference is

ΔHess = [O(t²) part of Δseagull] + 2⟨ΔV₂·S₀·V₀⟩ + 2⟨ΔV₁·∂_t(S V D_γ)⟩ + 2⟨ΔV₁ S₀ ΔV₁⟩ (schematically),

and none of these terms is forced to vanish (argument; the values are checked in §3.2).

**Lemma 4 (momentum forms; hermiticity; locality).**
- **S_M vertex and seagull.** An axis leg of any length along x from base b(n) carries (e^{iq_x n_x/M} − 1)e^{iq·b(n)}/d_x(q); with b(n) a linear map of n, Σ_nK(n)(·) is D_t at two corner points. Averaged over the 6 orders this gives `f4_lib.py:9-18`. The per-path diagonal seagull of an M-staircase depends on the leg bases only through differences b_r − b_r′ = (r − r′)n/M, so it is the same for all orders; by evenness of M_t every point it needs is a staircase corner (no extra flows).
- **Hermiticity.** The reverse of the order-σ M-staircase is the order-σ^rev M-staircase, so V^σ(q,0) = V^{σrev}(0,q) and the σ-average has V(q,0) = V(0,q). Checked: 8.1e-15 over M = 1, 2, 3, all σ, j, 400 points at t = 0.05 (`f4_slcheck.out:1`).
- **SL as the limit.** The σ-averaged staircase is a midpoint rule for the segment, so S_M → SL at O(1/M²). Checked against the direct SL forms V_j^SL = (q_j/d_j)∫₀¹∂_jD_t(sq)ds and N_j^SL = q_j²∫₀¹(1−u)∂_j²M_t(uq)du: the errors fall by factors 3.4-4.3 per doubling for M ≥ 8, reaching 2.5e-5 (vertex) and 2.0e-4 (seagull) at M = 32; M ≤ 4 is pre-asymptotic (ratios 1.0-1.6) (`f4_slcheck.out:2-10`).
- **Locality.** By reflection covariance, V_x(0,R_yq) = (a_x, −a_y, a_z, b)(q), so V_x is continuous across the zone face q_y = ±π only if a_y(q_x, π, q_z) = 0.
  - P: every corner has k_y ∈ {0, q_y}; near the face the D1 band is box-exact (W′ = 0 on |k| ≥ π − b), so a_y = 0 exactly there. Checked: 0 at q_y = π and π − 1e-3 (`f4_face.out:3-4`).
  - S_M (M ≥ 2): corners at k_y = rq_y/M sit in the Wilson region, and a_y ≠ 0 once t ≠ 0: 6.5e-5 at t = 0.05 for S2 and S4, and 0 at t = 0 (`f4_face.out:1-4`). So S_M and SL jump at the zone face at O(t): their couplings have power-law tails, i.e. they are non-local laws. This is the cost of the band-limited interpolation, and it is why F1 found "no closed momentum form" for local straight lines (`rF1:136`).
- **J and the straight line through the plaquette centre.** For every hop with |n_j| ≤ 1 (the 26 neighbours), the straight segment with the link field interpolated multilinearly between links gives the leg-base weights ∫(1−s)², ∫s(1−s), ∫s² = 1/3, 1/6, 1/3, exactly Psym's (`f4_face.out:5`). So J = the local straight line on those hops (proved); for longer hops they differ (not computed).

**Correction to F1's scope (`rF1:129`).** "The diagonal seagull at (q, −q) is path-independent" holds within the axis-ordered W-family, where each axis has one leg. It does not hold across families: S_M, SL and J have different diagonal seagulls, and the seagull carries most of the path dependence (§3.2). F1's ξ-argument (`rF1:188`, "whatever the path") concerns only the longitudinal contraction and stands.

### 3.2 (b) The Hessian per family

All values are ∂²_t δm/e² in SF units (×4 for R19-34's H-cov units), branch B1, R18-9 root unless stated, d = 0.003, nrk = 2, Richardson.

**Main table (R18-9 root).** H − H_P is computed on one grid for both families (exact cancellation at t = 0, Lemma 2), which is why the differences converge much faster than the Hessians themselves.

| family | local | Hessian (finest grid) | H − H_P | relative | convergence of H − H_P | source |
|---|---|---|---|---|---|---|
| **P** (Psym, F1) | yes | +2.4240125e-2 (344 nodes) and +2.4240272e-2 (240): F1's values on the same grids to all printed digits | — | — | 240 vs 344: 1.5e-8 | `f4_J344.out:5`; `f4_J240.out:5`; `rF1:200`; `P/scripts/C5/F1/f1_branches.out:2` |
| **J** (Psym-J) | yes | +2.43289e-2 (344) | **+8.879e-5** | **+3.663e-3** | 68/88/120/145/240/344 nodes: 9.59, 9.13, 8.86, 8.881, 8.880, 8.879 (×1e-5); 240 vs 344: 8e-9 | `f4_J344.out:6,8`; `f4_J240.out:8` |
| **S2** | no | +2.49472e-2 (145) | **+7.0830e-4** | +2.92e-2 | 120 vs 145 nodes: 8e-9 | `f4_A120.out:13`; `f4_B150.out:11` |
| **S3** | no | +2.49360e-2 (120) | +6.9028e-4 | +2.85e-2 | 88 vs 120: 1.1e-6 | `f4_A120.out:14`; `f4_c68fb.out:14` |
| **S4** | no | +2.53694e-2 (145) | **+1.13053e-3** | +4.66e-2 | 120 vs 145: 4e-8 | `f4_A120.out:15`; `f4_B150.out:12` |
| **S6** | no | +2.54911e-2 (120) | +1.24538e-3 | +5.14e-2 | 88 vs 120: 6e-8 | `f4_A120.out:16`; `f4_c68fb.out:16` |
| **S8** | no | | +1.3689e-3 | | 68 vs 88: 5.0e-6 | `f4_SL68.out:12`; `f4_SL88.out:12` |
| **S16** | no | | +1.6179e-3 | | 68 vs 88: 2.6e-6 | `f4_SL68.out:13`; `f4_SL88.out:13` |
| **S32** | no | | +1.6619e-3 | | 68 vs 88: 2.3e-6 | `f4_SL68.out:14`; `f4_SL88.out:14` |
| **SL** (M → ∞) | no | ≈ +2.591e-2 (F1's P + Δ) | **+1.674e-3 ± 0.4%** | **+6.9%** | 68 vs 88 nodes: 2.2e-6. Extrapolation: the S_M differences shrink 5.7× per doubling over M = 8, 16, 32; a 1/M² fit on (16, 32) gives +1.677e-3 and the fitted rate (1/M^2.5) +1.671e-3 | `f4_SL68.out:21`; `f4_SL88.out:21-22` |

- **The M-ladder is not monotone at small M** (S3 < S2; checked on three grids). M ≤ 4 is pre-asymptotic at the vertex level too (`f4_slcheck.out:5-6`); from M = 8 the approach to SL is asymptotic (vertex errors fall about 4× per doubling; the Hessian differences 5.7×).
- **Parts (145 nodes, `f4_B150.out:13-17`).** Change in the tadpole (seagull) Hessian: J +8.88e-5, S2 +7.84e-4, S4 +1.110e-3. Change in the family exchange: J 0 (same vertex), S2 −7.60e-5, S4 +2.04e-5; S32 (68 nodes) +3.9e-5 against a tadpole change of +1.625e-3 (`f4_SL68.out:15-19`). **The seagull carries 98-111% of every shift.** F1's single orderings share P's seagull and are not hermitian, so they probed only the exchange (`rF1:204`).
- **Step and RK steps (paired, same 80-node grid).** d = 0.003 with nrk = 2 against d = 0.0015 with nrk = 4: the differences agree to ≤ 4e-8 (J +9.3105e-5 vs +9.3132e-5; S2 +7.08583e-4 vs +7.08605e-4; S4 +1.133057e-3 vs +1.133096e-3), and P to 1.4e-7 (`f4_D2.out:10-12`; `f4_Dnrk4.out:10-12`).
- **0⁺ root** D1(0.915438682, 0.568280847), 116 nodes (`f4_C0p.out:5-12`): P +2.45373e-2 (F1: +2.45350e-2); J **+1.020e-4** (+4.2e-3); S2 **+7.551e-4** (+3.08e-2); S4 **+1.2020e-3** (+4.90e-2). Same pattern; the shifts are 6-15% larger than on the R18-9 root.
- **In R19-34's H-cov units (×4):** P +0.09696, J +0.09731, S2 +0.09979, S4 +0.10148, SL +0.1037. All have the opposite sign to R19-34's H-cov −0.04047 (`rR19-34:86`).

### 3.3 (c) Range, mixtures, and whether zero is reachable

**Range (checked).** Over every family computed, on the R18-9 root: H ∈ [+2.4240e-2, ≈ +2.591e-2 (P + Δ)] in SF units, i.e. +0% to +6.9% above Psym; ×4 = [+0.0970, +0.1037] in H-cov units. Local families only (P, J): [+2.4240e-2, +2.4329e-2], a spread of 3.7e-3 relative. Every value is ≥ 2.4e-2, 24 times the 1e-3 threshold of F1's FIXED readings.

**Mixtures (checked; the formula is exact: the seagull is linear and the exchange bilinear in the Wilson-line weights, `f4_lib.py:146-157`).** For U = (1 − λ)U_A + λU_B, H(λ) = H_P + Lλ + Qλ²:

| line | L | Q | zeros λ* | source |
|---|---|---|---|---|
| P ↔ J (local; same vertex, only the seagull moves) | +8.879e-5 | 0 (exact) | **−273.0** | `f4_J344.out:12`; `f4_J240.out:12` |
| P ↔ S4 | +1.13455e-3 | −4.02e-6 | **−19.95**, +301.9 | `f4_B150.out:19` |
| P ↔ S32 (≈ SL) | +1.6716e-3 | −9.68e-6 | **−13.5, +186** | `f4_SL88.out:23` |
| 0⁺ root, P ↔ J | +1.0198e-4 | 0 | −240.6 | `f4_C0p.out:20` |

- **Convex mixtures cannot reach zero (proved for these lines from the checked L, Q).** Q ≤ 0, so on λ ∈ [0, 1] the minimum of H is at an endpoint, and both endpoints are ≥ +2.42e-2.
- **Signed mixtures reach zero only far outside [0, 1].** A signed W-combination is still gauge covariant, cubic and hermitian, and the P ↔ J one is local. But it is not an average of paths: at λ* = −273 the hop's two-photon (F²) term is about 270 times the size any path average gives it.
- **Tuning.** Along P ↔ J, H = L(λ − λ*). F1's Earth-crossing row needs μ reduced to about 6e-9 of its value (`rF1:283`), so λ* must be held to 6e-9 relative, at every order of the loop expansion. Like κ* (P-R19-34b, `rR19-34:126-127,181`), this is a tuned zero of a law datum the registered texts do not fix. Priced below as P-F4a, not viable.
- **Other local families.** All-minimal-paths, Bresenham and multilinear straight lines beyond the unit cube were not computed (no closed momentum form). On the 26 unit-cube hops, J is the local straight line (Lemma 4). The large S_M/SL shifts come with the band-limited (non-local) field interpolation; whether a local straight line on long hops moves the Hessian as much as SL is not known. J, which equals the local straight line on unit-cube hops, moves it by 0.37%; how much of SL's +6.9% comes from the band-limited interpolation and how much from long hops was not separated.

**Sizes (arithmetic, scaled from F1's canonical, conditional mapping; F1's mapping is linear in the Hessian, `rF1:247-252`).** Factor H/H_P: J 1.0037, S2 1.029, S4 1.047, SL 1.069.
- Earth-crossing exceedance (F2 row 1, both signs): 1.6e8 (P) → 1.61e8 (J) … 1.71e8 (SL).
- m_g²/H² at 100 GeV: +7.6e13 (P, J) … +8.1e13 (SL); massive sign, as in F1.
- Earth |m_g|: 3.6e-9 eV → 3.6e-9 … 3.7e-9 eV.
- The sign is the same in every family, so F1's sign reading (massive under R19-34's convention) is family-independent.

**Subtractions (d), carried over from F1 (proved, by construction).** P-R19-34a resets the critical mass on every uniformly strained law, so δm(t) ≡ δm(0) whatever the gauge paths; it covers every family. P-R19-31b (ψ̄ψ as an (S_loc) background) acts on the source side and is likewise path-blind. Neither is adopted.

## 4. Against the FIXED readings (`TESTS:9276-9279`), literal first

| reading | status |
|---|---|
| **PATH-INVARIANT** | **Not met.** The closest family (J, local) differs from P by 3.66e-3 relative and the others by 2.9e-2 to 6.9e-2 relative, against the 1e-6 line (checked; the J and S2 differences are converged to ≤ 1e-8 absolute). No proof of invariance exists; Lemma 1 shows why: families differ by field-strength couplings, which the loop photon sees at P = 0 |
| **PATH-SHIFTS** | **Met (worker).** Range +2.4240e-2 to ≈ +2.591e-2 (P + Δ) e² (SF units; +0% to +6.9%); local families +0% to +0.37%. Zero is **not** reachable by any convex family computed; it is reachable only by tuned signed mixtures (λ* ≈ −273 local, λ* ≈ −13.5 with SL), priced as P-F4a (not viable) |
| OPEN | Not met. Every family was built, satisfies Ward (6.7e-16), and converged. What is not computed (local families without closed forms) is stated in §1 and §6 |

**Worker reading: PATH-SHIFTS.** Small for the local alternative (0.37%), a few percent for the band-limited straight line (+6.9%), the same sign in every family, and no untuned zero. F1's SF-HAZARD reading is unchanged in every family; its sizes move by at most 1.069×.

## 5. Against the expectation (`TESTS:9280`)

- **"PATH-SHIFTS":** borne out.
- **"At a small level":** partly. For the local alternative J the shift is 0.37%. For the straight Peierls line it is +6.9%, which is 400 times F1's single-ordering spread.
- **"Path dependence enters through the transverse photon coupling inside the loop, which is not zero at zero external momentum":** borne out (Lemma 1, Consequence 2). The specific channel is mostly the transverse **two-photon** (seagull) coupling, not the one-photon vertex: the seagull carries 98-111% of each shift.
- **"F1 already found the single orderings within 4e-6 of Psym, which suggests a small spread":** not borne out as a guide. Every axis ordering has the same diagonal seagull (`rF1:129`, correct within that class), so the single-ordering probe varied only the exchange. Families outside the axis-ordered class move the seagull, and the shift is 20-400 times larger.

## 6. Strong words

- **"Proved"** (short, unrefereed): Lemma 1 (field-strength form of every family difference; ξ-independence for every family); Lemma 2 (all families equal at t = 0); Lemma 3 (O(t²) onset); Lemma 4 (S_M momentum forms, σ-independence of the M-staircase seagull, hermiticity, SL as the M → ∞ limit at O(1/M²), the zone-face continuity criterion, J = local straight line on unit-cube hops; the S_M jump itself is checked, not proved); convex mixtures cannot reach zero along the computed lines; P-R19-34a covers every family.
- **"Checked":** every number in §3, with the grids and sources stated. M = 1 reproduces F1's library to 7e-18.
- **"Converged":** differences H − H_P across grids to ≤ 6e-8 absolute for J, S2, S4, S6, 1.1e-6 for S3 and 2-5e-6 for S8-S32 (§3.2 column), and ≤ 4e-8 under the step/RK change; the SL value rests on the 68- and 88-node grids (agreeing to 2e-6) and on the M → ∞ extrapolation (±0.4%: 1/M² against the fitted rate).
- **"Every family":** only those in §1's table. **Not computed:** local lattice families without a closed momentum form (all minimal paths, Bresenham staircases, multilinear straight lines beyond the unit cube, staple-detoured off-axis hops); fat links on axis hops (they change R19-34's t = 0 law); the J-type versions of S_M; two loops; T₂g.
- **"Local":** P and J are local laws (their vertices are continuous on the torus; checked at the face). S_M (M ≥ 2) and SL jump at the zone face at O(t) (checked) and are non-local; I include them because the item names the straight-line family and because they bound what a straighter path does.
- **F1 correction (scope only):** `rF1:129`'s path-independence of the diagonal seagull holds within the axis-ordered class, not across families.

## 7. Prices (named, not adopted)

- **P-F4a (new; not viable): a signed gauge-path mixture tuned to the zero.** U = (1 − λ*)U_W + λ*U_J with λ* ≈ −273 on the root's edges (local), or λ* ≈ −13.5 toward SL (non-local). 1 tuned number per edge per order; needs about 6e-9 relative precision for F2's Earth row. Same class as P-R19-34b (κ*): a tuned zero of a law datum the registered texts leave free. It is a different datum (the path weight of the SF law, not the Wilson placement of the H-cov law), so it is listed separately; neither is viable.
- **No other new price.** P-R19-34a (counted once) still covers the channel in every family.
- **The path family itself is an unfixed law datum** (reading): the registered texts fix the strained law only up to it, as F1 already noted (`rF1:136`). It moves the Hessian by +0.4% to +6.9% in the families computed. No registered text selects one; Psym remains the unique choice among one-leg-per-axis W-averages (`rF1:128`).
- **No axiom text changes.**

## 8. Files (`S/` = `scratchpad/C5/F4/`)

- `scripts/f4_lib.py`: the path families (momentum forms in the docstring), `pieces()` (base, tadpoles, bilinear exchange), mixtures. Imports `scripts/f1_lib.py` (F1's, unmodified copy) and `arch/` (unmodified).
- `scripts/f4_validate.py` → `f4_validate.out`: F1 reproduction, Ward, t = 0 equality.
- `scripts/f4_slcheck.py` → `f4_slcheck.out`: hermiticity of the σ-average; S_M → SL at O(1/M²).
- `scripts/f4_face.py` → `f4_face.out`: zone-face continuity (locality); multilinear weights.
- `scripts/f4_run.py` → `f4_coarse68.out`, `f4_c68fb.out`, `f4_A120.out`, `f4_B150.out` (grids), `f4_C0p.out` (0⁺ root), `f4_SL68.out`, `f4_SL88.out` (M = 8, 16, 32 and SL), `f4_D2.out` + `f4_Dnrk4.out` (paired step/RK check), `f4_J240.out`, `f4_J344.out` (J on F1's grids). Raw integrals: `raw_<label>.json`.
- `scripts/queue*.sh`: the sequential run queues (one heavy process at a time). `scripts/t_flow.py`: a timing/RSS probe of one flow.
- Unused copies from F1's directory (`f1_*.py` other than `f1_lib.py`) are kept for provenance and were not run.

