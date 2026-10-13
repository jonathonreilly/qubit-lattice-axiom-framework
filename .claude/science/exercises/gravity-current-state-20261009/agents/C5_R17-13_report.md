# C5 R17-13 report: the Wilson-Dirac T₂g shear row μ_T2. Can it be zeroed with SM content, and at what cost?

**Author.** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. Unrefereed. Ran 2026-10-13 01:37Z to 02:18Z. No repository file was edited. No downloads and no web lookups.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `S/` = `.../scratchpad/C5/R17-13/`. My scripts and `.out` files are in `S/scripts/`.
- `S/arch/` holds unmodified copies of `P/scripts/C5/R17-9/*.py` and `verified_VM*.npy`.
- Every run used `OMP_NUM_THREADS=2`. The longest single run took 331 s (`solve4_C.out`). The machine load was 4–8 from other jobs.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `P/TESTS.md`:
  - the C5 method and readings (`:2302-2320`);
  - the R14-3 entries (`:4830-4844`, `:4915-4923`), R16-1 (`:5041-5061`, `:5246-5250`, `:5416-5422`), R16-9 (`:5373-5397`, `:5550-5556`, `:5668-5684`), R16-13 (`:5595-5613`, `:6088-6108`, `:6146-6157`), R17-4 (`:5816-5845`, `:5940-5946`, `:6171-6178`) and R17-9 (`:6110-6128`, `:6267-6282`);
  - my item, `:6365-6383`;
  - the round-18 overlap note at `:6413` (R17-13 owns μ_T2).
- `P/agents/C5_R16-13_report.md` (all), `C5_R16-13_referee_verdict.md` and `C5_R16-13_referee.md` (`vR16-13`).
- `P/agents/C5_R17-9_report.md` (all). Its referee finished while I ran (`scratchpad/C5/ref_R17-9/REFEREE_VERDICT.md`, `vR17-9`): **CONFIRMED WITH CORRECTIONS**. The reading is OPEN with VM out of setting, and SM-LIFTED if VM is admitted. After a small N = 128 retune of the VM root, μ_T2 = 0.106187 (`vR17-9` item 3).
- `P/agents/C5_R16-1_report.md` §§0–3.4 and its verdict; `C5_R14-3_report.md` §§0–3.2 and its verdict.

**Labels.** proved (a complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **μ_T2 is not sign-definite on D1, so the expectation fails (proved in one limit; checked across the family).**
   - On R14-1's subluminal D1(b, r) Wilson-Dirac edges the T₂g shear mass takes both signs at fixed light mass m = 0.01 and at m = 0.001:
     - it is negative for weak Wilson terms (every b at r ≤ 0.3, and large b at any r);
     - it is positive for strong Wilson terms on wide slabs (b ≲ 0.9 at r ≳ 0.45).
   - In the weak-Wilson limit the sign is proved: μ_T2^F = r⁴C₄ + O(r⁵) with C₄ < 0 (Lemma S, §3.3).
   - The archived data already showed both signs:
     - `C5_R16-13_report.md:187-190` has negative μ_T2^F on D1 at m = 0.01;
     - R17-9's D1 range is [−1.2e-4, +1.6e-2] (`C5_R17-9_report.md:215`).
   - The "Wilson mass coupling directions" mechanism the expectation names is real, but it is only the positive MM piece. The kinetic–Wilson interference piece (KM) is negative and of the same size.
2. **An explicit subluminal zero exists (checked; ZEROED on the letter).** With r fixed at the R17-9 VM root's r = 0.55962727, only the Dirac box b_f moves:
   - **m = 0.01:** D1(b* = 0.916719266558, r = 0.55962727) has μ_T2^F = 0. Five independent quadratures give |μ_T2^F| ≤ 9e-10. The two pieces it cancels between are ±7.4e-4.
   - **m = 0.001:** D1(b* = 0.901017317054, r = 0.55962727).
   - **Subluminal:** r < 1/√3, so v_max ≤ 1 over the whole zone (Lemma V1, `C5_R16-13_report.md:176-179`). Sampled v_max = 0.999999.
   - **Transversal:** ∂μ_T2/∂b = −1.46e-3 per Dirac field. So the zero costs exactly **one continuous Dirac-edge tuning**.

   The zero set is a curve in the (b, r) plane. It runs from (0.15, 0.318) to (0.949, 1/√3) at m = 0.01 (§3.4).
3. **A closed form (proved; checked to ≤ 1e-6 relative).**
   - μ_T2^F = (N_c/2)⟨q_x q_y/E⟩, with q_j = W′_j p_j.
   - Its IBP twin: μ_T2^F = (N_c/6)⟨E³W″_xW″_y⟩ − (N_c/2)⟨E W′_x²W′_y²⟩.
   - Neither form has a fixed sign. R16-1's convexity route (Lemma K) does not transfer, because q_j changes sign across each slab.
4. **(c) The 4-row SM-count root was not found (search, not a proof).**
   - R17-9's VM content is 4 scalars on one G_w edge, 22.5 Dirac fields on one Wilson edge, and 12 VM vectors on one γG_w edge.
   - Putting its Dirac edge on the μ_T2 = 0 set breaks the μ_E balance.
     - On the D1 zero curve, the 22.5 Dirac fields give μ_E = −0.16 to −0.40.
     - The scalar and photon edges supply at most +0.064 while the T₂g row is also met (sampled ranges, §3.5).
   - Weak-Wilson DG edges (R16-13's flat-plateau family) were also tried. Six local solves (7 knobs, 4 rows, or r slaved to the true zero branch) all stalled at family bounds:
     - the photon box b_γ → 0.15;
     - the scalar at its μ_E maximum;
     - or the r → 0 corner, where μ_T2 vanishes only as r⁴ and the doublers become light.
   - With r held on the true zero branch, the best end point leaves (Ξ_T2g, Ξ_Eg, μ_E) = (−1.0e-2, +5.8e-4, −4.8e-3). Runs with r merely small reach (−3.6e-3, +1.4e-3, +1.7e-3), against row scales up to 0.95, but there μ_T2 is only r⁴-small, not zero (§3.5).
5. **Cost.**
   - μ_T2 alone is one Dirac-edge shape tuning. It is a shape row, not a separate non-shape knob.
   - Combined with R17-9's three rows at SM counts in these families, it was not met.
   - The rows conflict through μ_E: the shape that zeroes μ_T2 makes the Dirac sea's μ_E 5–11× more negative than at the VM root.

**Against the FIXED readings (`TESTS:6378-6381`).**
- **Worker reading: ZEROED on the letter of the clause.** The clause asks for an explicit subluminal law with μ_T2 = 0, checked. That is met, at two light masses.
- **The (c) part: 4-row root not found.** So the SM-content version of the plain question ("with SM content", `TESTS:6365`) stays **OPEN**. The referee should rule whether the title's "with SM content" makes (c) part of the clause. If it does, the reading is OPEN, by the precedent of `vR16-13` item 5.
- **SIGN-DEFINITE: not met, and false on D1 and on DG.** Both signs occur (checked). Lemma S fixes the sign only asymptotically (r → 0), with no explicit class bound.

---

## 1. Class, stipulations, exclusions (stated before any title)

- **Dirac edges.** 4-component Wilson bands, E² = Σ_j s(k_j)² + M², with M = m + Σ_j W(k_j). Here s is odd and 2π-periodic with s(π) = 0, and W is even with W ≥ 0. Two families are used.
  - **D1(b, r)** (R14-1, as coded in `S/arch/dirac.py` and `content3.D1q`):
    - s′ = 1 on [0, b], 1 − 2 sstep((k − b)/w) on [b, π − b], and −1 on [π − b, π], with w = π − 2b;
    - W′ = r√(1 − s′²), the Gevrey step sstep (`sublum.py`).
  - **DG(b, w, r)** (R16-13, `C5_R16-13_report.md:79`): D1 with a flat s′ = 0 plateau, where W′ = r.
  - Both are subluminal on the whole zone for r ≤ 1/√3 (Lemma V1, `C5_R16-13_report.md:176-179`, confirmed in `vR16-13` item 4).
  - Both are **mirror-symmetric**: s(π − k) = s(k) and W′(π − k) = W′(k). This is the hypothesis of Lemma S.
- **Shear: SF**, as R16-13 stipulated (`C5_R16-13_report.md:90-97`; P-R16-13a).
  - μ_T2^s = −½⟨H_xy p_x p_y/E⟩, with p = ∇(E²/2) and H = Hess(E²/2).
  - Dirac sea: μ^F = −N_c μ^s[E], with N_c = 4.
  - μ_T2^F depends only on the band E(k) and on SF. **It does not depend on V0, U, VU or VM.** So probes (a), (b) and ZEROED are independent of R17-12's placement question. Only (c) uses VM.
- **Content for (c)** (R17-9, `C5_R17-9_report.md:60-65`):
  - 4 real scalars on G_w(b_s, w_s) with the U vertex;
  - 22.5 Dirac fields on one Wilson edge with V0;
  - 12 massless vectors on γG_w(b_γ, w_γ) with VM;
  - all with SF and m = 0.01.

  The evaluators are R17-9's archived photon and scalar runners, used unmodified, plus my own Dirac evaluator (`lib13.dirac_rows`, checked against `dfam` and `vR16-13`).
- **Supplied zero-point vacuum or filled sea, one loop.** In the empty Fock vacuum μ_T2 ≡ 0, as for every quantity here.
- **Excluded:** superluminal edges; pairing; Clifford-flat 8-component fermions (μ_T2 ≡ 0 there, but they enlarge the site fibre, P-R16-13b); off-axis q; two loops.
- **Locality (round-18 rule, `TESTS:6403`).** SF is a strain response, not a TT vertex. V0's own Lemma-M locality is R18-3's subject (`TESTS:6415`) and is not tested here.

## 2. Prior art (each counted once)

- **R16-13** (`vR16-13`: OPEN). It contributes:
  - the mechanism: H_xy = W′_xW′_y defeats the separable Liouville zero (`C5_R16-13_report.md:171-174`);
  - the price wording: "one more tuning per Wilson-fermion edge" (`:272`).

  The referee's caution that H_xy ≢ 0 is "not a universal nonvanishing proof" (`vR16-13` item 3) is now borne out: the row can be tuned to zero.
- **R17-9** (`vR17-9`). It contributes:
  - μ_T2 = +0.106 at the VM root (`C5_R17-9_report.md:248`);
  - one 4-row start that ended at the bounds (`:249`);
  - the D1 range of both signs (`:215`).

  That range already implies a D1 zero by continuity. What is new here: the zero is located, verified, explained (Lemma S) and tried in the 4-row system.
- **R16-1 Lemma K** (`C5_R16-1_report.md:149-170`). A convexity sign argument works there because Ω(·; 0) = 0 and Ω is convex, so the integrand vanishes off supp W and is positive on it. Here the analogous factor q_j changes sign inside supp W′ (§3.2), so no such route exists.
- **R14-3 (R1)** (`C5_R14-3_report.md:86-88`). The K₄ IBP form of μ_E. My form I is the T₂g analogue for a non-separable band.
- **Grep.** I searched `P/agents` and `TESTS` for "μ_T2", "T₂g shear", "mirror" and "C₄". There is no prior closed form, sign lemma or located zero for the Wilson-Dirac μ_T2.

---

## 3. Results

### 3.1 Rechecks (checked; `check1.out`)

My independent evaluator (`lib13.py`) builds s and W by per-node Gauss–Legendre integration, with no tables, and integrates on the positive octant. It agrees with the archived numbers:

| law, m | lib13 form P | IBP form I | archived dfam | prior record |
|---|---|---|---|---|
| D1(1.4, 0.3), 0.01 | −1.15955267e-6 | −1.1595537e-6 | −1.159525e-6 | −1.15955e-6 (`vR16-13` item 3) |
| D1(1.4, 0.3), 0.3 | +4.3604906e-7 | +4.36045e-7 | +4.360711e-7 | +4.4e-7 (`R16-13:187`) |
| D1(1.4, 1/√3), 0.01 | −1.2798416e-5 | −1.2798430e-5 | −1.279805e-5 | −1.28e-5 (`R16-13:190`) |
| vR16-13 retuned root D1(1.313475, 0.572783), 0.01 | −3.52766137e-5 | −3.5276642e-5 | −3.527546e-5 | −3.52766e-5 (`vR16-13` item 3) |
| R17-9 VM root D1(0.384833, 0.559627), 0.01 | +4.7148090e-3 | +4.7148085e-3 | +4.714812e-3 | ×22.5 = 0.106083 (`R17-9:248`); `vR17-9`'s retune gives 0.106187 |

The Dirac rows (Ξ_T2g, Ξ_Eg, μ_E, μ_T2) from `lib13.dirac_rows` on D1(1.4, 0.3) at m = 0.01 are (+5.46009e-3, +2.82914e-3, −2.91855e-2, −1.15955e-6). They equal `vR16-13` item 2 to all printed digits.

### 3.2 (a) Closed forms (proved; checked)

**Form P.** Under SF, with p_j = s_js′_j + MW′_j and H_xy = W′_xW′_y:

  μ_T2^F = −N_c·(−½)⟨H_xy p_x p_y/E⟩ = (N_c/2)⟨q_x q_y/E⟩, with q_j := W′_j p_j = W′_j s_j s′_j + M W′_j².

Each q_j is even in k_j. Write q = K + Mq_M, with K_j = W′_j s_j s′_j (kinetic) and the mass part MW′_j². This splits μ_T2^F = KK + KM + MM:
- **MM** = (N_c/2)⟨M²W′_x²W′_y²/E⟩ > 0. This is the "Wilson mass coupling directions" piece.
- **KK and KM** carry the factor s s′. On D1 and DG it is antisymmetric about π/2, so these pieces have no fixed sign a priori.

**Form I (IBP).** Assume W is periodic and C², or W′ is absolutely continuous.
1. p_y/E = ∂_yE and p_x = ∂_x(E²/2).
2. Integrate by parts in k_x:

   X := ⟨W′_xW′_y p_x p_y/E⟩ = −½⟨E W″_xW′_y p_y⟩ − ½⟨E W′_x²W′_y²⟩ + ½X.

   This uses ∂_x∂_yE = H_xy/E − p_xp_y/E³.
3. Then ⟨E W″_xW′_y p_y⟩ = ⟨W″_xW′_y ∂_y(E³/3)⟩ = −⅓⟨E³W″_xW″_y⟩.
4. Hence

   **μ_T2^F = (N_c/6)⟨E³ W″_x W″_y⟩ − (N_c/2)⟨E W′_x² W′_y²⟩.** ∎

The second term is ≤ 0. The first is an E³-weighted W″–W″ correlation of indefinite sign, because ⟨W″⟩ = 0 per direction. Forms P and I agree to ≤ 1e-6 relative on every law in `check1.out`.

**Why R16-1/K-type convexity does not apply (reading backed by proof).** R16-1's integrand vanishes off supp W and is positive on it. Here q_j changes sign inside supp W′, at the maximum of s (s′ = 0, k = π/2 on D1). Lemma S below shows that the negative interference terms dominate for weak W, and the scan shows that MM dominates for strong W on wide slabs.

### 3.3 (b) Sign: Lemma S (proved) and the sign map (checked)

**Lemma S (weak-Wilson sign).**
- **Hypotheses (class 𝒲_mir):**
  - s is odd, 2π-periodic and C², with s(π − k) = s(k) and s′ ≥ 0 on [0, π/2];
  - W = r ŵ, with ŵ even, 2π-periodic, C² and nondecreasing on [0, π], and ŵ′(π − k) = ŵ′(k);
  - s ≥ s₀ > 0 on supp ŵ′ ∩ [0, π];
  - N_c = 4, SF.

  D1 and DG satisfy all of these.
- **Claim:** μ_T2^F = r⁴ C₄(m) + O(r⁵), with

  C₄ = (N_c/2)⟨A_xA_y(−E₀⁻³ + 3m²E₀⁻⁵) + (A_xB_y + A_yB_x)(E₀⁻¹ − m²E₀⁻³) + m²B_xB_y E₀⁻¹⟩,

  where A = ŵŵ′ss′, B = ŵ′², and E₀² = m² + Σs².

  **C₄(0) < 0.** By continuity, C₄(m) < 0 for small m.
- **Proof.**
  1. Expand q_xq_y and 1/E in r. On the support of q_xq_y, E₀ ≥ √2 s₀, so the expansion is uniform.
  2. **Mirror step.** Put f = ss′, so f(π − k) = −f(k), while ŵ′ and every function of s² are symmetric about π/2. Then every term in which an x- or y-factor carries no ŵ weight integrates to zero. This removes the O(r²) and O(r³) terms and leaves the displayed O(r⁴) terms.
  3. **Sign step.** For k ∈ [0, π/2], A(k) + A(π − k) = ŵ′f·[ŵ(k) − ŵ(π − k)] ≤ 0, because f ≥ 0 there and ŵ is nondecreasing. Hence ⟨A·g⟩ ≤ 0 for every g ≥ 0 that is symmetric about π/2, strictly if g > 0.
  4. **Cross term.** With g = B_y/E₀ for fixed (k_y, k_z), 2⟨A_xB_y/E₀⟩ < 0.
  5. **AA term.** h(k_y, k_z) := ⟨A_x E₀⁻³⟩_x ≤ 0 is symmetric in k_y, so ⟨A_y h⟩ ≥ 0, and the AA term −⟨A_xA_y/E₀³⟩ ≤ 0.
  6. At m = 0 the m² terms vanish. ∎
- **Checked** (`c4check.out`). μ_T2^F/r⁴ → C₄ linearly in r at b = 0.15, 0.385, 0.9 and 1.4, with m = 0 to 0.3. For example:
  - b = 0.385, m = 0: C₄ = −4.8261e-2, and μ/r⁴ = −4.8221e-2 at r = 0.01;
  - b = 1.4, m = 0.01: C₄ = −1.5501e-4, and μ/r⁴ = −1.5492e-4.
- **Scope.** This is an asymptotic sign with no explicit r₀(b, m), so it does not meet SIGN-DEFINITE.

**Sign map on D1** (`scan1.out`; GL 4×12, stable to ≤ 1e-9 relative against 6×16):

| m = 0.01 | r = 0.05 | 0.1 | 0.3 | 0.5 | 0.56 | 1/√3 |
|---|---|---|---|---|---|---|
| b = 0.15 | −4.9e-7 | −7.1e-6 | −6.1e-5 | **+5.4e-3** | **+1.15e-2** | **+1.40e-2** |
| b = 0.40 | −2.8e-7 | −4.2e-6 | −1.22e-4 | **+1.85e-3** | **+4.43e-3** | **+5.52e-3** |
| b = 0.80 | −8.5e-8 | −1.3e-6 | −6.9e-5 | −1.2e-5 | **+2.9e-4** | **+4.3e-4** |
| b = 1.00 | −3.5e-8 | −5.5e-7 | −3.4e-5 | −1.09e-4 | −8.0e-5 | −5.8e-5 |
| b = 1.40 | −9.6e-10 | −1.5e-8 | −1.2e-6 | −7.8e-6 | −1.16e-5 | −1.28e-5 |

m = 0.001 has the same pattern (`scan1.out`).

Parts at r = 0.56 and m = 0.01 (KK, KM, MM):

| b | KK | KM | MM |
|---|---|---|---|
| 0.3 | −3.8e-5 | −3.42e-3 | +1.02e-2 |
| 0.9 | −1.4e-5 | −7.77e-4 | +8.19e-4 |
| 1.4 | −7.7e-8 | −1.5e-5 | +3.6e-6 |

The sign is decided by the KM–MM balance. The same holds on DG: `dgman.out` has 54 (b, w) points, each with one sign change in r.

### 3.4 ZEROED: the explicit law (checked; `verify_zero.out`)

**Main law, m = 0.01: D1(b* = 0.916719266558, r = 0.55962727).**

| check | value |
|---|---|
| lib13 form P (GL 4×12 / 8×16 / 12×24) | +2.2e-12 / −7.8e-19 / +8.1e-14 |
| IBP form I (12×24) | −8.9e-10 |
| archived dfam GL (3,8) / (6,12) | +1.1e-8 / +3.3e-12 |
| archived uniform 3D grid (`dirac.strain_mu`), N = 160 / 240 | +4.1e-10 / +2.0e-11 |
| parts it cancels | KK −1.28e-5, KM −7.247e-4, MM +7.374e-4 |
| transversality | ∂μ_T2^F/∂b = −1.4617e-3; ∂μ_T2^F/∂m (fixed law) = +2.5705e-3; db*/dm = +1.76 |
| subluminality | r < 1/√3, so whole-zone v_max ≤ 1 (Lemma V1, proved); sampled v_max (81³) 0.999999 |
| doublers | W_π = 0.35366, so doubler rest energies are m + n·0.354, n = 1..3 |
| tails | Gevrey-class step, so faster than any power (reading, as R16-1); not computed |
| other Dirac rows (V0 + SF, per field) | Ξ_T2g +4.3474e-3, Ξ_Eg +1.2469e-3, μ_E −1.7230e-2 |

**Second light mass, m = 0.001:** D1(0.901017317054, 0.55962727). The zero holds to the same accuracy in all five checks. W_π = 0.36215. The Dirac rows are (+4.3136e-3, +1.1874e-3, −1.6930e-2).

**Further zeros:**
- at r = 0.5, b* = 0.790523229542 (m = 0.01) and 0.773750762247 (m = 0.001);
- r*(b) at m = 0.01: 0.3178 (b = 0.15), 0.3704 (0.385), 0.4006 (0.5), 0.5509 (0.9) (`curve2.out`);
- there is no zero at r ≤ 1/√3 for b ≳ 0.949.

**m-transfer (proved).** On supp q_x q_y, E ≥ √2 b > 0, so μ_T2^F is real-analytic in m through m = 0. With m = 0 explicitly allowed by this bound, a law tuned at m → 0 leaves residual |μ_T2^F| ≈ 2.6e-3·m per field at light mass m. That is ≲ 3e-20 per field at m a ≲ 1e-17 (reading at a = ℓ_P, `AX:189-190`). The drift is linear in m, as `vR16-13` item 4 found for the Wilson cone rows.

### 3.5 (c) The 4-row SM-count solve: not found (search; sampled necessary conditions)

**Necessary conditions on the D1 zero curve** (`curve1.out`, `curve2.out`, `scalmax.out`, `photgrid.out`, `cloud.out`).
- Along μ_T2^F = 0 with b_f ∈ [0.15, 0.95], the per-field Dirac rows are:
  - Ξ_T2g ∈ [+3.9e-4, +4.5e-3];
  - Ξ_Eg ∈ [−4.5e-3, +1.4e-3];
  - μ_E ∈ [−1.78e-2, −7.2e-3].
- So 22.5 Dirac fields put μ_E at −0.16 to −0.40. At the VM root it was −0.0345 (`curve1.out:1`).
- The scalars give at most 4μ_E^s ≤ +0.063. The U-vertex G_w maximum is +1.584e-2 per scalar at b_s → π (`scalmax.out`).
- Every VM photon with μ_E^γ ≳ 5e-3 has Ξ_γ,T2g ≳ +0.02 (`photgrid.out`), which breaks the T₂g row.
- Over all 112 × 91 scalar × photon grid pairs, the best 4μ_E^s + 12μ_E^γ meeting the T₂g row within 25% is +0.064 (b_f ≤ 0.25). For b_f ≥ 0.8 no pair meets the T₂g row at all.
- The shortfall is a factor 2.5–6 (checked on samples; not an enclosure).

**Weak-Wilson DG edges** (`dgman.out`, `cloud.out`, `solve4*.out`).
- On the DG zero manifold, r* ∈ [0.020, 0.47] and W_π ∈ [0.04, 0.19].
- The Dirac rows can have Ξ_Eg ≪ 0 and small μ_E. Then the photons must supply T/Eg ≈ 0.2–0.37 at Eg ≈ 0.03–0.08. The VM γG_w family reaches that ratio only at Eg ≳ 0.07, where its μ_E^γ > 0 again breaks the μ_E row.
- Local solves (photon N = 48; Dirac GL (3,8); 7 knobs, 4 rows):

| run | constraint on r | end point | residual (Ξ_T2g, Ξ_Eg, μ_E) | binding |
|---|---|---|---|---|
| A, B | free (lower bound 0.01) | DG(1.02, 0.02, r ≈ 0.010) | (−9.8e-3, +9e-4, −5.3e-3) | r → 0 (μ_T2 ∝ r⁴, W_π ≈ 0.011: near-naive doublers); photon b_γ → 0.15; b_s → 3.1 |
| C, D | r ≥ 0.03 | DG(0.31–0.33, 0.51, r = 0.030–0.034) | (−3.6e-3, +1.4e-3, +1.7e-3); μ_T2 −1.6e-6 (only r⁴-small) | r at its bound; Dirac/vector parts of ±0.3/±0.95 cancel |
| E, F | slaved to the nontrivial μ_T2 = 0 branch | E: DG(0.46, 0.22, 0.063); F: DG(1.02, 0.022, 0.049) | E: (−3.4e-2, +1.2e-2, +1.1e-2); F: (−1.04e-2, +5.8e-4, −4.8e-3) | F: photon b_γ = 0.150 (bound; under-resolved at N = 48), scalar b_s = 3.099 (μ_E max) |

- **Reading.** Within R17-9's families, the μ_T2 = 0 condition and the μ_E condition compete for the same quantity, the Wilson-mass weight of the Dirac sea.
  - On D1, the μ_T2 zero needs the KM–MM balance, which forces μ_E^F ≈ −(0.7–1.8)e-2 per field.
  - Weak-Wilson DG shifts the burden to the Ξ rows and the photon's T/Eg curve.
- **Scope.** Samples and local solves only. No enclosure. The photon small-box corner (b_γ < 0.2) is under-resolved, as `vR17-9` item 5 also notes. Not tried:
  - scalar families beyond G_w (for example R16-3 zigzags);
  - photon shapes beyond γG_w;
  - two Dirac edges;
  - non-mirror-symmetric Wilson profiles (outside Lemma S).

### 3.6 (d) Prices and the bill (named, not adopted)

- **P-R17-13a (μ_T2 as a shape row).** Under SF, zeroing μ_T2 costs one continuous Dirac-edge tuning (b_f or r) per Wilson-Dirac edge.
  - Its precision comparator is R16-3's ~1e-13 relative (`C5_R16-3_report.md:276`; comparator).
  - One tuning at m → 0 covers every light species on that edge to O(m) (§3.4).
  - **This confirms R17-9's bill row "μ_T2: 1" as a shape tuning, not a non-shape knob** (`C5_R17-9_report.md:274`).
- **P-R17-13b (the conflict price, suggested).** At SM counts in R17-9's VM content and families, the μ_T2 tuning is not compatible with the other three rows (not found). Any of the following would buy it:
  - a non-shape shear knob (R16-9's P-R16-9a counterterm);
  - Clifford-flat 8-component fermions, which give μ_T2 ≡ 0 but enlarge the site fibre against `AX:47` (P-R16-13b);
  - wider scalar or photon edge families (scalar μ_E^s ≳ 0.04 per scalar would be needed with D1);
  - weak-Wilson Dirac edges with light doublers (W_π → 0, the naive-fermion corner R9-1 excludes).
- **Bill (conditional bookkeeping).** R17-9's 9 + CC per class / 13 + CC per species is unchanged in count. Its μ_T2 row is now an existing shape condition, but the joint 4-row point at SM counts is OPEN.
- **SF itself** remains stipulated (P-R16-13a; source/action gate `AX:187`; dynamics downstream `AX:114-130`).
- No axiom text changes. No sizes at a = ℓ_P are used beyond the one m-transfer reading.

---

## 4. Against the FIXED readings (`TESTS:6378-6381`)

**Worker reading: ZEROED on the letter. The SM-content 4-row root is OPEN (not found).**
- **ZEROED.** "An explicit subluminal law with μ_T2 = 0, checked." This is met:
  - D1(0.916719266558, 0.55962727) at m = 0.01, and D1(0.901017317054, 0.55962727) at m = 0.001;
  - |μ_T2^F| ≤ 9e-10 in five evaluators, against cancelling parts of ±7.4e-4;
  - transversal; subluminal by Lemma V1.

  The clause's second sentence, "If (c) succeeds, also report the full 4-row root", is conditional. (c) did not succeed, so no 4-row root is reported.
- **SIGN-DEFINITE: not met, and false as expected.** D1 and DG take both signs at fixed light mass (checked, three evaluators). Lemma S proves a negative sign only as r → 0.
- **OPEN** applies to the SM-content question in the item's title. If the referee reads "with SM content" (`TESTS:6365`) as part of ZEROED, the reading is OPEN.
- **Expectation** ("SIGN-DEFINITE on D1 (positive) … a separate knob", `TESTS:6383`): **false.**
  - The positive Wilson-direction piece (MM) is real, but the kinetic interference piece (KM) is negative and dominates for weak W, which Lemma S proves.
  - μ_T2 is a shape-tunable row. It is not a separate non-shape knob in isolation. At SM counts it competes with μ_E.
- **Removed hypothesis** ("μ_T2 = 0 at one loop", R16-9). Removing it costs one tuning per Wilson-Dirac edge in isolation. Jointly with R17-9's rows at SM counts, the cost is open.

## 5. Strong-word check

- **"Proved"** is used only for:
  - Form P (definition plus SF);
  - Form I (IBP);
  - Lemma S (asymptotic, with hypotheses stated);
  - real-analyticity of μ_T2^F in m through m = 0 (support bound E ≥ √2 b);
  - the existence of a zero by continuity between checked opposite signs;
  - Lemma V1 subluminality, which is R16-13's lemma, cited.
- **"Checked"** means three independent quadratures (lib13 GL, archived dfam GL, archived uniform grid) plus the IBP form, at several resolutions.
- **"Not found"** means local least squares from the stated starts plus sampled ranges. There is no global search and no enclosure. It is **not a CONFLICT claim.**
- **"Every / all"** refers to the sampled grids (90 D1 laws per mass, 54 DG zero points, 112 scalars, 91 photons).
- **Not claimed:**
  - SIGN-DEFINITE;
  - a 4-row root;
  - any VU statement;
  - V0 locality;
  - non-mirror Wilson profiles;
  - dressed or two-loop effects.

## 6. For the referee

1. **Form I's IBP** (§3.2) and **Lemma S's mirror and sign steps** (§3.3). In particular, check that every O(r²) and O(r³) term has an unweighted antisymmetric factor.
2. **The zero** (`verify_zero.out`). Rerun D1(0.916719266558, 0.55962727) at m = 0.01 with an independent quadrature.
3. **Whether ZEROED is met by a single-edge zero** when (c) fails, given the title's "with SM content".
4. **§3.5's sampled μ_E budget on the D1 zero curve.** Is an enclosure (μ_E^F ≤ −7e-3 per field on the whole curve; scalar μ_E^s ≤ 0.016 on U-G_w) reachable? That would make the D1 part of (c) a certified conflict in these families.

## 7. Files (`S/scripts/`)

- **`lib13.py`.** The independent evaluators:
  - D1 and DG laws built by GL integration;
  - μ_T2^F in forms P and I;
  - the KK/KM/MM split;
  - the full Dirac rows (`dirac_rows`).
- **`check1.{py,out}`:** rechecks against the archived values and the referee values.
- **`scan1.{py,out}`:** the sign map, the parts, and b*(r).
- **`c4check.{py,out}`:** Lemma S against the numerics.
- **`curve1.{py,out}`, `curve2.{py,out}`:** the D1 zero curve, with the Dirac rows along it.
- **`verify_zero.{py,out}`:** the ZEROED law, five evaluators, transversality, v_max and W_π.
- **`dgscan.{py,out}`, `dgman.{py,out,npy}`:** the DG zero manifold.
- **Grids:**
  - `scalmax.{py,out}`, `scalgrid.{py,npy}`: scalar ranges;
  - `photgrid.{py,out,npy}`: VM photon grid at N = 48;
  - `cloud.{py,out}`: candidate and necessary-condition search.
- **Solves:**
  - `solve4.py` → `solve4_{A,B,C,D}.out`, `root4_*.npy`;
  - `solve4s.py` (r slaved) → `solve4s_{E,F}.out`, `root4s_*.npy`.
- **`S/arch/`:** unmodified copies of R17-9's runners.
