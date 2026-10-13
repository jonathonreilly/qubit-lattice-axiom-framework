# C5 S26: synthesis after rounds 17–18 (refereed: R17-9 … R17-13, R18-1, R18-2, R18-4 … R18-8, R18-10; worker readings R18-9, R18-11; R18-12, R18-13 running)

**Author and provenance.** Claude Opus 5.5 (S26). This is the same model family as every C5 worker, the supervisor, and S5–S23. **This synthesis is not refereed and gives no verdicts.**
- Every verdict quoted is from codex gpt-5.6-sol at xhigh, as recorded in `TESTS` or in the cited `agents/` verdict file.
  - The R18-7 and R18-8 referee runs show `model: gpt-5.6-sol` and `reasoning effort: xhigh` in their `codex_run.log` headers (`SP/ref_R18-7/codex_run.log:5,9`; `SP/ref_R18-8/codex_run.log:5,9`). Their verdicts appeared at `SP/ref_R18-7/REFEREE_VERDICT.md` (03:22Z) and `SP/ref_R18-8/REFEREE_VERDICT.md` (03:29Z) and were read at about 03:33Z.
  - Both were absent when checked at 03:16Z and 03:21Z. vR18-7 was then recorded at `TESTS:7020-7027` (03:37Z), in agreement with the `SP/` file; **vR18-8 is not yet recorded in `TESTS`.** Both are used here as [ref]. §§1–9 were updated for them, and for the R18-9 … R18-13 records (`TESTS:6978-7091`), at 03:33Z–03:55Z.
  - The R18-10 referee (`SP/ref_R18-10/codex_run.log:5,9`: gpt-5.6-sol, xhigh) wrote `SP/ref_R18-10/REFEREE_VERDICT.md` at 03:42Z; it was read at about 03:48Z and is **not yet recorded in `TESTS`**. It is used here as [ref].
- Written 2026-10-13, about 03:17Z to 03:55Z. No repository file was edited.

**Read in full.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`).
- `agents/C5_S23_synthesis.md` (`S23`), the base. Its structure is followed here.
- `TESTS:6108-6391`: the R17-9 … R17-13 registrations, worker readings and the 01:11Z/01:38Z verdict records.
- `TESTS:6392-7091`: everything from "C5 Round 18" on, including the 02:16Z, 03:00Z and 03:17Z verdict records and the R18-9 … R18-11 registrations. The records at `:6978-7091` (R18-10 worker; R18-12 registration; vR18-7; R18-11 and R18-9 workers; R18-13 registration) were added at 03:37Z–03:41Z and read at 03:40Z–03:43Z.
- Referee verdicts: `C5_R17-9`, `C5_R17-10`, `C5_R17-11`, `C5_R17-12`, `C5_R17-13`, `C5_R18-1`, `C5_R18-2`, `C5_R18-4`, `C5_R18-5`, `C5_R18-6` (`_referee_verdict.md`), and the full R18-6 verdict `C5_R18-6_referee.md` (`refR18-6`).
- The R18-7, R18-8 and R18-10 verdicts in `SP/` (`REFEREE_VERDICT.md` for each); findings 6–8 and the strongest statement of the full R18-8 verdict (`SP/ref_R18-8/C5_R18-8_referee_verdict.md:140-198`); grep hits in the full R18-7 verdict (`SP/ref_R18-7/R18-7_independent_referee_verdict.md`).

**Read in part.**
- Price sections:
  - `rR17-9:264-289`, `rR17-10:257-265`, `rR17-11:263-273`, `rR17-12:276-282`, `rR17-13:265-278`;
  - `rR18-1:223-233`, `rR18-2:273-292`, `rR18-4:305-314`, `rR18-5:298-320`, `rR18-6:156-178`, `rR18-7:244-252`, `rR18-8:174-182`.
- Reading and plain-words sections: `rR17-12:286-300`, `rR17-13:282-296`, `rR18-1:21-40`, `rR18-2:26-60`, `rR18-5:36-60,324-348`, `rR18-6:41-72`, `rR18-7:1-110`, `rR18-8:1-70,140-200`. After 03:40Z: `rR18-10:1-51,221-257` and `rR18-11:1-72,134-162,196-281` (its worker reading is recorded at `TESTS:7028-7043`). Also `rR18-9:277-322` (off-axis rows and prices).
- Line checks: `rR16-14:152` and `C5_R16-14_referee.md:16` (the O(G²) closure claim); `SUMMARY:677-714` (§26, label fix now applied); `PRICE_NOTE:1-6,263-413` (v6 delta).
- R18-9 … R18-11 reports were read only in the parts listed above. R18-12 and R18-13 have no reports yet.

**Pending at about 03:50Z.**

| Item | State | Where |
|---|---|---|
| R18-7 (set A completion N as a construction) | **referee: CONFIRMED WITH CORRECTIONS, CONSTRUCTED** in the weak-field harmonic static/quasi-static scope; recorded at `TESTS:7020-7027` | `TESTS:6713-6736` (registration), `:6898-6916` (worker); `vR18-7` |
| R18-8 (W7 at infinity) | **referee: CONFIRMED WITH CORRECTIONS, ANOMALY met**; **not yet recorded in `TESTS`** | `TESTS:6751-6778`, `:6943-6954`; `vR18-8` |
| R18-9 (four cone/shear rows with SM content, conserved vertices) | **worker reading FOUR-ROW-ZERO on the letter** (4 tunings + a narrow photon window; off-axis unpaid); referee running | `TESTS:6847-6869`, `:7044-7059`; `rR18-9` |
| R18-10 (dipole-conserving Z₂ ensemble) | **referee: CONFIRMED WITH CORRECTIONS, OPEN** (no pinch; the dipole is six label totals); **not yet recorded in `TESTS`** | `TESTS:6871-6897` (registration), `:6978-6986` (worker); `vR18-10` |
| R18-11 (set A E1 + N in Poisson gauge; premise (iii)) | **worker reading OPEN with a NOISE-OVERSHOOT candidate**; referee running | `TESTS:6920-6942`, `:7028-7043`; `rR18-11` |
| R18-12 (relic edge quanta; the W7 bound; whether P-W7edge0 holds dynamically) | pre-registered 03:37Z; worker running | `TESTS:6988-7019` |
| R18-13 (off-axis graviton rows at the SM root) | pre-registered 03:40Z; worker running | `TESTS:7061-7091` |

**Paths and abbreviations.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS`, `SUMMARY` and `PRICE_NOTE` are in `P/`.
- `rX` = `P/agents/C5_X_report.md`. `vX` = `P/agents/C5_X_referee_verdict.md`. `refR18-6` = `P/agents/C5_R18-6_referee.md`.
- `vR18-7` = `SP/ref_R18-7/REFEREE_VERDICT.md` and `vR18-8` = `SP/ref_R18-8/REFEREE_VERDICT.md` (referee outputs in the scratchpad, not yet copied to `agents/`). `refR18-8` = `SP/ref_R18-8/C5_R18-8_referee_verdict.md` (the full R18-8 findings).
- `vR18-10` = `SP/ref_R18-10/REFEREE_VERDICT.md` (likewise in the scratchpad, not yet in `agents/` or `TESTS`).
- `SP/` = the session scratchpad's `C5/`. `AX` = the axioms memo. `S23` = `P/agents/C5_S23_synthesis.md`.

**Labels.**
- **[ref]**: referee-confirmed, within the referee's scope.
- **[ref, bounded: class]**: a refereed FAIL, EXCLUDED, OBSTRUCTED, CONFLICT or no-go, with its class.
- **[worker]**: a worker claim the referee did not confirm or has not ruled on.
- **[pending]**: R18-12 and R18-13 (no reading yet), and the R18-9 and R18-11 referees.
- **[S26 reading]**: an interpretation made here. Same model family; unrefereed.

**Sets** (as S8–S23). A = continuum base, discreteness only in records. B = Euclidean Z⁴. C = the axioms' Z³ with continuous time, tuned. C-box = Z³ × ℝ with a box-exact law. C-box-S = C-box with boson–fermion pairing per cell. **C-box-E** (named in R18-6) = C-box with site creation, √h fixed per site and R14-5's E-sector (the arena of class 𝒟, `vR17-11:44-45`).

**Record-keeping notes.**
- `TESTS` now runs to 7091. The latest verdict record is vR18-7 (`:7020-7027`, 03:37Z); the 03:17Z record (R18-1, R18-5, R18-6) is at `:6956-6977`.
- `SUMMARY` still ends at §26 (`SUMMARY:677-714`). Its label fix for R15-4/R15-6 is now applied in the text ("Label corrected 2026-10-13"), so S23's carried correction is closed.
- Archive fixes since S23: the R17-7 runner (`TESTS:6625`) and the R17-8 runner, plus an audit of every archived runner's `sys.path` inserts (`TESTS:6745`). See §5.

---

## 1. What changed since S23, in plain words

### 1.0 The short version

S23 ended with three things unpriced or half-priced: a produced graviton; Λ as an added principle with three conditions; and a cone bill whose Standard-Model (SM) line turned on a half-cell placement of the photon's magnetic stress. Since then:

1. **The vertex placements S23 relied on are gone, and so is the Dirac vertex. What replaced them supports a conditional SM root.**
   - Consistency (the forward Ward value, "Lemma F", plus covariance) excludes both photon placements, VU and VM [ref, bounded: R13-5's symmetric universal-energy W1 class, O(q); `vR17-12:17,19`].
   - It also excludes R16-13's Dirac vertex V0 [ref, bounded: same class; `vR18-5:3`].
   - The surviving vertices are the per-leg-averaged vector family VW and the Dirac vertex UD. UD is unique only inside a stipulated family 𝔇 (`vR18-5:7`).
   - With them, SM counts (4 scalars + 22.5 Dirac + 12 vectors) zero the two axis cone rows and the E_g shear at m = 0.01 with 3 tunings, **if a signed VW stencil is admitted**. μ_T2 ≈ 0.0911 stays unpaid [ref, conditional; `vR18-5:9-22`].
   - R16-13's "Dirac birefringence" obstruction was a property of V0, not of conserved Dirac vertices (`vR18-5:7`).
2. **μ_T2 is a shape row, not a separate knob** [ref, R17-13 ZEROED; `vR17-13:13,17`]. At SM counts, whether it can be zeroed together with the other three rows is OPEN (`vR17-13:15`). [worker, R18-9; referee running] It can: at SM counts all four axial rows vanish together with 4 tunings (scalar edge, Dirac b_f and r, and the signed stencil a = −0.176), plus a narrow photon window b_γ ≈ 2.936–2.947 that may count as a fifth. The Dirac edge sits on R17-13's zero curve. The off-axis rows stay unpaid, and UD has face2 ≠ T₂g (about 7e-5 per field) (`TESTS:7044-7059`). R18-13 counts the off-axis rows [pending].
3. **The three Λ/β pieces fit together only if N is restated.**
   - Literal N (the metric sourced by total stress, vacuum included) conflicts with (d-i) whenever the vacuum enthalpy W ≠ 0 on an expanding slice [ref, bounded: JOINT-CONFLICT in class 𝒟; `vR18-6:5,11`].
   - With N restated as N_red, sourced by matter plus "vacuum minus the lowest state", the triple (S) + (d-i) + N_red is exactly classical GR on T_m − (V − e₀)g. It gives β = γ = 1, Λ̃ = 0 under P93, and no Lemma-S channel, in three clauses and zero fitted numbers [ref, conditional; `vR18-6:3,13`].
   - N_red is a new completion, not a wording fix (`vR18-6:5`; `refR18-6:26`). The quantum step (J2: gravity's own zero-point inside "the lowest state") is OPEN (`vR18-6:7`).
4. **(S)'s particle-physics test is OPEN, not failed.** SM-only absolute stability needs M_t(pole) ≤ 170.88 GeV at two loops [ref; `vR18-2:5`]. The recalled inputs favour metastability at 1.48–3.09σ depending on how the pole-mass ambiguity is treated. That is not a robust > 2σ conflict, so the reading is OPEN (`vR18-2:7`).
   - The lattice cannot stabilize the vacuum in the tested H-EFT class (`vR18-2:9`).
   - A Higgs-portal singlet stabilizes it at the cost of one unprotected scalar-mass tuning. Chirally protected vector-like 5-plets (n5 ≥ 2) stabilize it with none (`vR18-2:11,13`).
5. **The qubit window: one gap in the obstruction closed; the screening question is open.**
   - Theorem Z₀ [ref, bounded: uniformly Lieb–Robinson-local, cubic-covariant, unique symmetric ground state, local E⊕T₂ readout, strict vector gap]: a gapless tensor branch that the readout sees statically forces a pinch point in **every** f-sum class (`vR18-1:11`). R17-6's k⁰ gap is closed in that class.
   - Whether finite charge fugacity always screens the pinch point is OPEN. No pinch point was seen through βU = 4, and βU ≤ 3.5 looks screened, but βU = 4 is not equilibrated and βU = ∞ is frozen (`vR18-1:3,9`).
   - [ref, R18-10 OPEN; `vR18-10:15`] Conserving the γ-dipole does not help. It equals six global label totals and imposes no local Gauss law; the fixed-dipole sector is screened with R18-1's ξ. Planar conservation laws can fake an axis pinch, so pinch claims need off-axis checks (`vR18-10:3,7,11`). The referee adds that "a pinch needs S_γ = o(k²)" is right for the registered test but should not be universalized to the total charge structure factor (`vR18-10:13`).
6. **W15 lost another hole.** Two-band analytic band crossings, Weyl points included, cannot carry redshifting momentum [ref, bounded: EXCLUDED-CROSS; `vR18-4:13,15`]. Still open: continuous multi-shift mixing, N > 2 braiding, joint mixing with field dependence.
7. **(d-i) is refereed CONSISTENT; its bill reduction is conditional bookkeeping** [ref; `vR17-11:39,44-45`]. The receiver (site creation with √h fixed per site) is a model postulate, not derived from the lattice axioms (`vR17-11:22-23`). The "universal (d-ii) no-go" was overclaimed (`vR17-11:36`).
8. **Two more results came back from the referee during this synthesis** (03:22Z and 03:29Z; vR18-7 recorded at `TESTS:7020-7027`, vR18-8 not yet).
   - **W7 at infinity** [ref, R18-8 ANOMALY; `vR18-8:3,25`]: the asymptotic Poincaré charges fail the algebra by the defect charge of edge quanta already at degree 2, {K_b, P_c} = δ_bc H + Q_D,cb, and no completion beginning at degree 3 can cancel it. The far-field signature is a velocity-dependent, anisotropic combination √(E² − P²) of the translation charges. It is not an invariant mass (`vR18-8:19`). Thermal populations make it tiny below about 1e18 GeV under stated assumptions; relic populations are not bounded.
   - **Set A** [ref, R18-7 CONSTRUCTED in scope; `vR18-7:26`]: E1 + N_c is a causal, conserved, order-by-order records-to-metric law through O(G²) in harmonic gauge, with β = γ = 1 and a CP instrument. It needs three new stipulations: a conserving projection Π (causal but not spatially local), a gauge, and a noise insertion weight a. R16-14's unprojected N is genuinely non-conserving. N̄ is not a linear quantum channel (`vR18-7:3-11`).
9. **A worker reading arrived after 03:35Z: set A's record noise overshoots at the one gauge-independent insertion** [worker, R18-11; `TESTS:7028-7043`; referee running].
   - Only the insertion a = 2, the record read as √−g T^{μν}, makes the averaged noise source independent of the readout gauge (Theorem G). On Minkowski the noise's mean energy is pinned at its zero start (Lemma P), so only its pressure acts (`rR18-11:134-156`).
   - At a = 2 the active density is negative and exceeds ρ_Λ in size over all of R15-2's window, by ×1.17 to ×1e19 (a NOISE-OVERSHOOT candidate). R18-7's a = 4 zero fails once the noise depends on time, carries T_⊥ noise, changes gauge, or starts from zero (`rR18-11:27-43,245-251`).
   - A suggested twist, not built: in FRW the noise may settle into a positive cosmological constant, equal to ρ_Λ near ℓ ≈ 3.7 µm at the longest allowed gain time (`rR18-11:211-216`). R19-2 drafts the test.

**[S26 reading], the one-sentence picture.** S23's picture holds and has sharpened. Every remaining item is a source/observable bridge question (`AX:85-90,187`), and round 18 showed which bridges can be stated together:
- what gravitates: (S) + (d-i) + N_red, three clauses and no number, classically;
- what the metric is in set A: N_c, three more stipulations [ref, in scope]; and, at the one gauge-independent insertion, a noise budget that overshoots unless the S/V channels are under-recorded [worker, R18-11];
- which vertex couples matter to the graviton: U, UD, VW, plus law data;
- which global charges are physical, and which measurement reads them: P141 or P142 for W7 [ref].

The graviton is still the one thing with no construction at any price except supplying it (P-N1). Its window now has a theorem-level static signature (Z₀) and an open screening question.

### 1.1 The cone vertices and the SM bill (W3, W4, W11, new W19)

- **R17-9: CONFIRMED WITH CORRECTIONS. Reading OPEN with the imported placement; SM-LIFTED only if VM and its G_w photon are admitted as extra stipulations [ref; `TESTS:6582-6585`; `vR17-9:13`].**
  - VU is representative-invariant, with the correct continuum Maxwell amplitude. It is absolutely summable and quasi-local, not finite-range (`vR17-9:3`).
  - The Dirac-like vector sign is confirmed as a sampled claim, not a theorem (`vR17-9:5`).
  - The archived VM root missed zero under tighter quadrature (μ_E = −4.75e-5). A small retuning restored it, with μ_T2 = 0.106187 (`vR17-9:7`).
  - No enclosure excludes a VU solution; sign changes already occur near b_γ = 0.1 (`vR17-9:11`).
- **R17-12: CONFIRMED WITH CORRECTIONS. Both FORCED labels are met through their exclusion disjuncts; substantively NEITHER [ref, bounded: R13-5's symmetric universal-energy W1 class, necessary O(q); `TESTS:6795-6801`; `vR17-12:19`].**
  - **Lemma F:** W1 plus a symmetric stress fixes the forward stress, F^ij = ωv_iv_jδ. It is a necessary O(q) condition, not an exact completion (`vR17-12:5`).
  - **VU fails it.** Residuals 0.304–1.135 against required scales 0.022–0.062 on independent samples (`vR17-12:7-11`).
  - **VM fails twice.** Its E_g row fails Lemma F, and its one-sided magnetic placement breaks C₂ covariance about R9-9's h_xy (defects about 14–29% at q = 0.3) (`vR17-12:13`).
  - **What survives: VW.** W1 fixes the q = 0 T₂g vertex to VM's value. Covariance replaces VM's one-sided placement with a symmetric VW stencil. Normalized symmetric stencils differ by identically conserved superpotentials, so their O(q²) placement is free (Lemma I). No exact W1 completion was constructed (`vR17-12:15`).
  - **Registration collision.** The fixed fork assumed one of VU, VM survives. The referee records both FORCED labels via exclusion, annotated NEITHER (`vR17-12:17`).
- **R18-5: CONFIRMED WITH CORRECTIONS. V0-FAILS confirmed; SM-LIFTED-CONSERVED if signed VW stencils are admitted, which the referee reads the unqualified setting as allowing; otherwise OPEN [ref; `TESTS:6964-6968`; `vR18-5:22`].**
  - **V0 fails Lemma F.** At an independent check point it gives +0.2654 where −0.2654 is required. Open off-box regions, especially mixed central/mirror boxes, carry an O(1) defect (`vR18-5:3`).
  - **Lemma M′:** spinor covariance permits a nonzero face amplitude. Lemma M's zero applies to scalar legs only (`vR18-5:5`). So V0 fails conservation, not locality.
  - **UD = ½(p_j∂_ih + p_i∂_jh)** is the unique forward-correct vertex within the stipulated strain-flow family 𝔇. It couples the Wilson mass. The family restriction, the pair block, the O(q²) placement and exact W1 completion are not derived (`vR18-5:7`).
  - **UD's birefringence** spans −5.19e-4 to +2.40e-3. So R16-13's sign obstruction is V0-specific (`vR18-5:7`).
  - **The SM root** (4 + 22.5 + 12, one Higgs edge, all subluminal): (Ξ_T2g, Ξ_Eg, μ_E) = (1.57, 3.93, −0.014)e-6 at the stored point (N = 160), drifting to about (8.2, 7.8)e-6 at N = 192. This is a nearby transversal numerical zero, paid by 3 tunings (`vR18-5:9-14`).
  - The signed stencil has weights 1.1227446 and −0.1227446, with P(0) = 1. It is local and covariant (`vR18-5:16`).
  - **Unpaid:** μ_T2 ≈ 0.0911, off-axis closure, exact conservation (`vR18-5:22`). Off-axis rows for vectors and Dirac fields were not computed (`rR18-5:348`).
- **R17-13: CONFIRMED WITH CORRECTIONS. Reading ZEROED; the four-row SM problem OPEN; SIGN-DEFINITE false [ref; `TESTS:6802-6805`; `vR17-13:17`].**
  - Forms P and I are exact under SF (`vR17-13:5`).
  - Lemma S holds only with an added overlap hypothesis (Ŵ′ss′ ≢ 0), which gives C₄(0) < 0 (`vR17-13:7`).
  - D1(0.916719266558, 0.55962727) at m = 0.01 has a transversal μ_T2 = 0, with ∂_bμ_T2 = −1.46e-3. That is one continuous edge-shape tuning (`vR17-13:9,13`).
  - Within SF, μ_T2 depends on the band, not on the vertex (V0/U/VU/VM) (`vR17-13:11`).
  - At that zero, μ_E^F = −0.0172 per field (−0.388 for 22.5 fields). The 2.5–6× deficit against available positive μ_E is search evidence, not an enclosed bound (`vR17-13:15`).
- **R17-10: CONFIRMED WITH CORRECTIONS. K₆ OPEN, μ_E OPEN, JOINT not met [ref; `TESTS:6586-6589`; `vR17-10:53`].**
  - Theorem F is valid on the conditioned fast face (u = 1, b ≥ 2.9935m, s_min ≥ 1.3768m). It persists locally around each realizable sharp-turn skeleton (`vR17-10:37`).
  - It does not earn CERTIFIED-CONFLICT, even qualified "on 𝓕", because the clause needs the whole superset (`vR17-10:33`).
  - The μ_E remark excludes only constant-multiplier pointwise certificates (`vR17-10:49`).
- **[S26 reading] What the vertex results do to the bill.**
  - Every Dirac Ξ number from R16-13 to R17-12 used a non-conserved vertex (V0). Every VU or VM vector number used a non-conserved or non-covariant vertex. The rows they fed are re-derived only by R18-5.
  - R18-5's root is the first SM-count axial zero on vertices that pass the forward test and covariance. It still depends on three items of law data that nothing fixes:
    - the signed VW stencil (P129);
    - the Dirac pair block, through the family 𝔇 (P133);
    - the Dirac O(q²) placement (P134) [worker].
  - The count does not change: the three rows were already counted (`S23:357-358`). The payment changed: one of the three tunings is a placement datum, not a shape. No pairing is used.
  - **R18-9 [worker; referee running] closes the axial rows and opens the off-axis ones.** All four axial rows vanish at SM counts with 4 tunings plus a photon window (P147). The mechanism: μ_T2 comes only from the Dirac fields, so the Dirac edge must sit on R17-13's zero curve; the signed stencil decouples the photon's Ξ from its μ_E. For UD, face2 ≠ T₂g (−6.7e-5 at m = 0.3, +7.2e-5 at m = 0.1 per field), so the fermion off-axis rows are not inherited from the axis rows. VW's off-axis extension is undefined (a further law datum) (`rR18-9:277-297`). R18-13 counts them [pending].

### 1.2 One source bridge (W9, W10, W17, new W18)

- **R17-11: CONFIRMED WITH CORRECTIONS. Central result survives: CONSISTENT in the stipulated class [ref; `TESTS:6590-6600`; `vR17-11:44-45`].**
  - Q_ν = ∇^μ(W h_μν) cancels W exactly. W never enters λ̇ (generalized Lemma V). With nonzero shift there are zero residuals (`vR17-11:5-20`).
  - "Unique" means unique among pointwise stresses absorbable under H-imp, not among all receiver sectors (`vR17-11:20`).
  - The free spatial trace is a legitimate model postulate. It is not derived from site creation: the insertion law and any equation conjugate to site number are unbuilt (`vR17-11:22-23`).
  - No gravitational signalling at linear order, tilt included (`vR17-11:25-26`).
  - "Invisible" means exactly compensated, not physically absent. The Planckian vacuum inertia lives in a stipulated hidden compensator (`vR17-11:28-29`).
  - **Receiver exclusions, mixed** (`vR17-11:31-36`):
    - F1 (unimodular scalar): generic obstruction, confirmed;
    - F2 (matter): phenomenological arithmetic only;
    - F4 (P128): only for a single ultralocal P(X);
    - **F3 not confirmed: "(d-ii) still needs W = 0" is overclaimed.**
  - **Bill.** The tadpole row drops by one *numerical counterterm*, replaced by the stipulated, unforced P-vac′ bridge (`vR17-11:38-39`).
- **R18-6: NOT CONFIRMED (the JOINT-CONSISTENT). Literal reading JOINT-CONFLICT; modified net-source bridge consistent [ref, bounded: class 𝒟, connected expanding slices, W ≠ 0; `TESTS:6969-6977`; `vR18-6:13`].**
  - **J1.** Literal N, sourced by raw total matter-plus-vacuum stress plus gravitational self-stress, makes Bianchi require Q = 0. On a connected expanding slice that forces W = 0 (`vR18-6:5`).
  - **N_red** (the source is T_m − (V − e₀)g plus gravity's own stress) is consistent. It is "a new completion, not a wording correction" (`vR18-6:5`; `refR18-6:26`).
  - The conflict is narrow. It is escaped by W = 0, by a wholly static special configuration, by including the receiver in N's total, by adding another conserved receiver, or by abandoning the LL conservation identity (`refR18-6:28`).
  - **J2 (quantum).** Cubic *invariance* (not covariance) of the vacuum gives isotropy. The virial identification of ⟨t_LL⟩₀'s energy with the Hamiltonian zero-point holds only for free, gauge-fixed TT modes. The quantum claim is OPEN (`vR18-6:7`; `refR18-6:30`).
  - **Set A.** The registered (d-i) has no set-A receiver ("cannot be instantiated as registered", `refR18-6:34`). A Poincaré-invariant matter vacuum has W = 0. A scalar subtraction cannot remove a time-dependent or non-vacuum-form stress. The record-noise stress remains premise (iii). The 6ℓ²/r² filter correction is not a Bianchi defect (`vR18-6:9`).
- **R18-2: NOT CONFIRMED (the NEEDS-STABILIZER). Reading OPEN [ref; `TESTS:6806-6813`; `vR18-2:17`].**
  - M_t,crit = 170.8776 GeV, λ_min = −0.01129, λ_eff = 0 near 1.81e11 GeV, reproduced independently. The Buttazzo et al. fit gives 170.997 GeV (`vR18-2:5`).
  - The tension is 2.280σ on the primary row, with a flip at 0.644 GeV ambiguity. Plausible ambiguity treatments give 1.48–3.09σ, which is the registered inconclusive-input failure mode, hence OPEN (`vR18-2:7`).
  - **Lattice exclusion, scoped.** c₆^min = 4.37e11 and the conditional 2.6e108 ρ_Λ ratio reproduce. The 4.1e15 shortfall applies to the two dispersions computed. It is a scoped H-EFT/O(1)-coefficient result, not a universal no-go (`vR18-2:9`).
  - **Singlet.** One precision tuning per unprotected scalar species. The printed m_S ≤ 1.8e11 GeV window was a floating-point bug; consistency needs m_S < 3.17e10 GeV (`vR18-2:11`).
  - **Vector-like 5-plets.** n5 ≥ 2 stabilizes; n5 = 1 fails. The mass ceilings are not precision results (`vR18-2:13`).
  - **What (S) says.** (S) alone does not require our state to be exactly lowest. The true-minimum condition follows only after identifying the observed vacuum source with the uncompensated energy of our state above the law's ground (`vR18-2:15`).
- **R18-7 (set A completion N): CONFIRMED WITH CORRECTIONS. CONSTRUCTED, justified only in the stated weak-field harmonic static/quasi-static scope [ref; worker `TESTS:6898-6916`; `vR18-7:26`; recorded at `TESTS:7020-7027`].**
  - **N as written does not close at O(G²)** [ref]. `rR16-14:152` is wrong and Π is required. The worker's commutator and its 1.1–1.4(ℓ/R)² coefficient belong to a hybrid source, not to R16-14's literal filter placement; all three placements are generically non-conserving (`vR18-7:5-9`).
  - **The law E1 + N_c** [ref]: source S = (−g)J + Λ[h]; the retarded Π gives a causal, conserved, order-by-order law through O(G²); h₁ is E1 exactly. The LL equivalence is exact only through the retained O(G²) truncation. **Π is causal but not spatially local** (algebraic tails), so "K localized in the body" and "exterior vacuum up to erfc tails" are too strong (`vR18-7:3`). β = 1 from h₂⁰⁰ = 7M²/r² and h₂ᵏᵏ = M²/r²; γ = 1 is inherited; Π can add only an O(G²)/r mass renormalization (`vR18-7:13-18`).
  - **CP** [ref]: a measurement branch followed by a past-record-controlled unitary has Kraus operator U_rA_r, so the instrument stays CP. **N̄ is nonlinear in the input state, so it is not a linear quantum channel**, hence not CP in the standard sense; that alone does not imply trajectory-wise loss of positivity (`vR18-7:11`). This drops N̄ from owner Q2.
  - **Premise (iii), scoped** [ref]: the energy and active densities are (2a − 7)|u₁| and (2a − 8)|u₁|; the active one vanishes at a = 4. This covers only static, homogeneous scalar ρ-noise. It does not cancel the +|u₁| LL energy density or settle the T_⊥, vector, TT, time-dependent or FRW terms (`vR18-7:20`).
  - **Gauge caveat** [ref]: the quoted 7.44e28–2.77e35 is an energy ratio R(k); amplitudes differ by √R = 2.73e14–5.26e17. The Poisson-gauge metric-component kernel is not preserved, and there is no gauge-invariant time-dependent O(G²) noise result. This does not defeat the literal CONSTRUCTED clause (`vR18-7:22-24`). [worker, R18-11] Sharper: only a = 2 is gauge-independent.
  - **Aside** [worker, not ruled on]: a metric linear in the LL density variable gives β = 3 (`rR18-7:70-73`).
- **R18-11 (set A in Poisson gauge): worker reading OPEN, with a NOISE-OVERSHOOT candidate [worker; `TESTS:7028-7043`; `rR18-11:25-56`; referee running].**
  - **Theorem G.** For a record density of weight w, homogeneity plus the record's flat conservation give ⟨L_ξ𝔍⟩ = (w − 1)⟨(∂·ξ)𝔍⟩. So the mean source is independent of the readout gauge iff a = 2: the record is √−g T^{μν}. For R18-7's a = 4, harmonic and Poisson laws differ once the noise depends on time (`rR18-11:134-147`).
  - **Lemma P.** Any closing O(G²) law on Minkowski has a flat-conserved coarse-grained source, so the noise's mean energy density keeps its t₀ value, which is zero for E1 (`rR18-11:150-156`).
  - **The budget at a = 2.** The active density is exactly −4u₁ if the noise is taken as always present (reading (U)), and negative with size at least u₁ if it switches on from zero (reading (P)). |ρ_act| > ρ_Λ over R15-2's whole window, from ×1.17 at the top corner to ×1e19. Mercury excludes ℓ ≲ 2.5–2.7e-8 m locally (`rR18-11:196-210`).
  - **Escape.** The γ-trade (P-r15c) becomes necessary, γ_{S,V} ≤ ρ_Λ/(4u₁); otherwise a tuning to precision ρ_Λ/u₁ (`rR18-11:233-240`).
  - **Corrections to R18-7** [worker]: the a = 4 zero fails for time-dependent noise, T_⊥ noise, a change of readout gauge, and E1's zero-energy start. R18-7's "premise (iii): quantitatively no" becomes "yes, |ρ_act| ≥ u₁" at a = 2 (`rR18-11:245-252`).
  - **Suggested, FRW (not built).** The switched-on noise may tend to w = −1 with ρ ≈ (1 + ⟨x²⟩ + 2r + u_V/u₁)u₁/3, equal to ρ_Λ at ℓ = 3.65e-6 m at the τ_c ceiling (`rR18-11:211-216`).
- **[S26 reading] Where the bridge stands.**
  - **Classical, C-box-E: one package, refereed.** (S) + (d-i) + N_red is three clauses, zero numbers, exact GR outside the hidden compensator. "The law's lowest state weighs nothing; the vacuum's enthalpy goes to site creation; the metric is sourced by matter plus the vacuum's energy above the lowest state." The cost is that the third clause is new (P135), and the receiver is a model postulate (P52 inside H-imp).
  - **Quantum: one open step.** J2 asks whether gravity's own zero-point is in H and is removed the same way. Only free TT modes are covered. R19-3 drafts the test.
  - **Set A: a different package.** (S) + N_c [ref, in scope]. (d-i) cannot be instantiated, and is not needed for a Poincaré-invariant matter vacuum (W = 0, `vR18-6:9`). Set A's open budget is the record noise (premise (iii)). R18-7 makes its static scalar part a law choice (a) [ref, scoped]. [worker, R18-11] That does not survive a gauge-proper treatment: at the one gauge-independent insertion (a = 2), R15-2's overshoot returns as a candidate wall, and the escapes are the γ-trade or a tuning. Its suggested FRW twist (the record noise as the dark energy) is the most interesting open item in set A; R19-2 drafts it.
  - **The particle-physics prediction is unchanged in kind, sharper in number.** Under (S), with the vacuum-source identification of `vR18-2:15`, either M_t(pole) ≤ 170.9 GeV or there is new content below about 1e11 GeV.

### 1.3 Producing the graviton (W2)

- **R18-1: CONFIRMED WITH CORRECTIONS. (a)–(c) demoted to OPEN; (d) GAP-CLOSED for the strengthened, uniformly Lieb–Robinson-local class [ref; `TESTS:6958-6963`; `vR18-1:13`].**
  - The ensemble is covariant under the shift action (24/24 rotations) but not under the natural action (6/24). So it needs P112 (`vR18-1:5`).
  - Detailed balance and irreducibility hold within the declared coset. The L = 2 check compared energies only; the pre-registered S(k) comparison was not implemented (`vR18-1:5`).
  - The pinch diagnostic ρ = S_xz(k∥z)/S_xz(k∥y) is correct. The supplied Gaussian control was wrong as written (it used S_V/S_TT, with a 4/3 white-noise baseline); a corrected same-component control passes (`vR18-1:7`).
  - **Screening not established.** βU ≤ 3.5 is consistent with finite widths. At βU = 4 two independent L = 8 ladders gave (ξ²(q₁), ξ²(q₂)) = (14.4, 23.0) and (12.5, 10.9). So the fixed fork reads OPEN (`vR18-1:9`).
  - **Theorem Z₀** (`vR18-1:11`): in uniformly LR-local, cubic-covariant families with a unique symmetric ground state, a local E⊕T₂ readout and a strict vector gap, a statically visible gapless T₂ branch (Z/ω bounded below) forces a nonvanishing directional contrast, in every f-sum class. The contrast is bracketed by nested cutoff weights. It does not close the broader quasi-local H1 class.
- **[S26 reading]**
  - Z₀ turns the pinch point from "one option" (R17-6) into a requirement inside its class. Any qubit graviton with strict vector/scalar gaps and a statically visible tensor branch must show one, whatever its f-sum order.
  - The registered ensemble gives no evidence of one at finite fugacity. The exact limit is frozen under local moves (P130).
  - [ref, R18-10 OPEN; `vR18-10:15`] Conserving the γ-dipole on the moves fixes only six global label totals, and changes the static measure only by choosing a sector. The fixed-dipole sector is screened with R18-1's ξ (`rR18-10:12-22`; `vR18-10:3,5,7`). "Sector" here means the chain's communicating class; the registered moves are fragmented by 3L planar counts (3(L − 1) independent beyond the totals), and the repaired move set is proved ergodic only at L = 2 (`vR18-10:5,9`). So the fracton-like route as registered buys nothing static. A fracton-type Gauss law would have to be imposed on the states, which is P96 again (`rR18-10:36`).
  - [ref, R18-10; `vR18-10:11`] R18-1's axis-only diagnostic can be fooled: planar conservation laws give exact axis zeros while the off-axis channels stay screened (`rR18-10:33`). R18-1 reported no pinch, so its negative result is unaffected. Any positive claim must check face and body directions.
  - Production is untouched by statics. A static pinch point is necessary (Z₀), not sufficient. R19-1 drafts the dynamical step.

### 1.4 W15 (GW170817 as a gauge-invariant test)

- **R18-4: CONFIRMED WITH CORRECTIONS. EXCLUDED-CROSS [ref, bounded: nontrivial two-band real-analytic Bloch Hamiltonians on T³, free, symmetric-stress, projectable, canonical, regular field-dependent generators, H-RB assumed; `TESTS:6814-6825`; `vR18-4:15`].**
  - Lemma S0: momentum eigenvalues extend continuously through conical crossings, though eigenprojectors do not (`vR18-4:5`).
  - Theorem WX: on the (possibly disconnected) orientation double cover, every nonflat momentum-carrying branch has rank C ≤ 1. The Reeb step should use levelset-tame horizontal homology (`vR18-4:7`).
  - Lemma RB-X: H-RB forces rank C = 3 at degree-one conical and degree-two analytic extrema, not at arbitrary homogeneous order (`vR18-4:9`).
  - Lemmas X1/X2 need a parity correction: only factors with real curve branches have even multiplicity (x² + y² is a counterexample) (`vR18-4:11`).
  - Still open: continuous multi-shift mixing, N > 2 braiding, joint mixing with field dependence, interacting and other excluded classes (`vR18-4:3,15`).
- **[S26 reading]** W15 is now DERIVED for free finite-band local matter in every analytic form tried: the multiplier class, canonical altered generators, finite mixing, field-dependent generators on isolated bands, and two-band crossings. Its escapes are P64, P90, P124, or leaving the free/analytic/projectable class.

### 1.5 W7 (the off-box tail, at infinity)

- **R18-8 (W7 at infinity): CONFIRMED WITH CORRECTIONS. ANOMALY met [ref; worker `TESTS:6943-6954`; `vR18-8:3,25`; full findings `refR18-8:159-198`; not yet recorded in `TESTS`].**
  - **Theorem A (degree 2)** [ref]. In the stipulated Regge–Teitelboim phase space, the complete improved Killing generators have vanishing degree-1 pieces. So {K_b, P_c} = δ_bc H + Q_D,cb, with rotation-sector defect moments, while {K, H}, {K, K} and {P, P} close. Independently verified on a different band (residuals 2.1e-13–7.4e-13, against 0.032–1.94 for the Poincaré value). The worker's 2048-site check is a packet test, not an operator-norm identity (`vR18-8:5-7`).
  - **Lemma S∞: sign error** [ref]. {K_∂, Φ} = −Δ and {Φ, K_∂} = +Δ; the report used the second as the first. In the complete improved generator, bulk and surface cross-terms cancel, and the surviving +Q_D comes from the matter bracket (`vR18-8:9-13`). The anomaly survives; the worker's explanation of it is reversed.
  - **Lemma T** [ref]: off source, the tail is linearized gauge plus a Newtonian dipole with Ma_b = −Δ_cb. **Corollaries N and N′ are narrow:** N excludes only linear gauge-invariant metric functionals that keep the standard dipole response; N′ only continuous periodic one-body moments. Broader "no repair" language is not established (`vR18-8:15`).
  - **Theorem A3** [ref, conditional]: the Jacobi step is formally correct but needs a common differentiable domain, a boundary-preserving symplectomorphism and no boundary cocycle. F(Q_D) is conditional; the world-line contribution is unevaluated (`vR18-8:17`). A degree-2 anomaly already decides the fixed reading (`vR18-8:21`).
  - **Observable** [ref, corrected]: the small-velocity formula M(V) = M[1 − Q_D,bb V_b²/(2(E + Q_D,bb))] is right for E + Q_D,bb ≠ 0 (independent two-particle check). But once Poincaré closure fails, M(V) = √(E² − P²) is a frame-dependent functional of the translation charges, not an invariant rest mass. It is observable only under the fixed ADM/source/readout bridge (`vR18-8:19`; `refR18-8:145-151`).
  - **Size** [ref, conditional]: the thermal numbers assume a = ℓ_P, a thermal population, Earth's CMB speed and an implicit 1e-8 visibility scale. They support "thermally tiny below about 1e18 GeV under those assumptions", not an unconditional exclusion. Relic populations remain unbounded (`refR18-8:151-157`).
  - **Prices** [ref, narrowed]: P-W7anom is retained with the corrected leading-order wording. P-W7edge0 is an initial-state/domain condition preserved by the number-conserving model, not a derived state-selection rule (`vR18-8:23`; `refR18-8:171-176`). The worker's reduction of R17-2's P-W7bdy to P-W7anom rests on Corollary N, which is narrow.
- **[S26 reading]**
  - This moves W7 from "OPEN: degree 3 unclosed" to "the global charges carry the matter law's own lattice Lorentz violation", refereed at degree 2. That is SUMMARY §17's root, counted once (`rR18-8:32`), not a new effect.
  - The bulk reads as GR's dressing (R17-2, refereed); the boundary carries Q_D (R18-8, refereed). Together: W7 has no instantaneous bulk interaction. Its physical content is the edge-quantum population, plus the readout bridge that makes √(E² − P²) a measurement.
  - That makes the relic population the observable question. R18-12 (pre-registered 03:37Z, running; `TESTS:6988-7019`) tests it, including whether P142 holds dynamically.

### 1.6 The count (W11)

Rows are R13-8's P,T-even rows. Counting basis: per (spin, edge) class, then per species. Vertex basis: **U (scalars) + UD (Dirac) + VW (vectors)**, E1 extension, supplied zero-point vacuum.

| Row | Count | Status |
|---|---|---|
| Charged-matter cones | 3 per class / 7 per species | [ref, conditional; R16-2]. ≤ 2 only with P101 (an upper bound) [ref, R16-10]. Not re-solved for R18-5's photon and Dirac edges (`rR18-5:348`) |
| Graviton axis cone (E_g, T₂g) | 2 | [ref, conditional on signed stencils; `vR18-5:22`]. Paid at SM counts by 2 edge shapes + 1 VW stencil, jointly with μ_E (3 rows, 3 tunings) |
| Off-axis TT | 1 for U scalars (K₆); **≥ 1 more for UD Dirac** (face2 ≠ T₂g [worker, R18-9]); VW's off-axis extension undefined | [ref] one condition for scalars (`vR17-4:5`). K₆ jointly with the axis zeros OPEN; Theorem F on the conditioned fast face [ref, `vR17-10:53`]. [worker, R18-9] UD face2 − T₂g ≈ 7e-5 per field (`rR18-9:284-292`). R18-13 [pending] |
| E_g shear μ_E | 1 | Counted in the R18-5 three-row root [ref, conditional] |
| T₂g shear μ_T2 | 1 per Wilson-Dirac edge | [ref] a shape row in isolation (R17-13 ZEROED). [worker, R18-9; referee running] zeroed jointly with E_g, T₂g and μ_E at SM counts: 4 tunings + a photon window (P147) (`TESTS:7044-7059`) |
| LV tadpole (vacuum ρ + p) | 1 non-shape, or 0 numbers under (d-i) | [ref, `vR17-4:11`] for the 1. [ref, conditional bookkeeping, `vR17-11:38-39`] for the 0: a counterterm replaced by the stipulated P-vac′ bridge |
| CC | 1 tuned, or 0 numbers under (S) | [ref, `vR17-3:17`; `vR17-7:69`] |
| **Total** | **9 + CC per class / 13 + CC per species, as a lower bound** | [S23 reading], unchanged as a floor. With (S) and (d-i): 8 / 12 numbers plus two added rules. [S26 reading on worker R18-9] +1 if the photon window counts as a tuning; +1 or more for the fermion (and vector) off-axis rows. Plausible range 9–11 + CC per class, pending R18-13 |
| E2 extension | +1 | [ref] / [S26 reading] |

**[S26 reading]**
- Precisions are unchanged: about 1e-13 for the shapes and the stencil, 1e-16 for the charge rows. The R18-5 root is resolved only to about 1e-5 in the photon grid (`vR18-5:14`).
- **What the bill now rests on.**
  - Refereed rows on conserved, covariant vertices: the axis cone and μ_E (conditional), μ_T2 in isolation.
  - Unrefereed or uncomputed: the four-row joint point (R18-9, worker), the off-axis rows (R18-13), and a joint charge-plus-cone solve on the same edges.
- **What would lower it.** Nothing on record. Every favourable outcome so far changed *how* a row is paid, never *whether* it is paid.

---

## 2. Updated wall map

"DERIVED" means a refereed no-go or confirmed lemma in a stated class, including bounded EXCLUDED, FAIL, OBSTRUCTED and CONFLICT. "OPEN" means no refereed no-go covers the route's class and there is no PASS. "Cheapest named price" is the least expensive price on record that passes the wall. Nothing is adopted. Rows unchanged since S23 are carried with "(unchanged)".

| # | Wall | Refereed statement (scope) | DERIVED or OPEN | Cheapest named price | Axiom lines touched by that price |
|---|---|---|---|---|---|
| W1 | **Electron–photon split** (C, C-box, C-box-S) | No interval zero in 𝒬_lit⁻ (R13-7) or 𝒬_W⁺ ⊃ D1 (R16-1). Theorem L (R16-10). Literal class: Dirac zero with a v_max 7.35 photon (R16-10) | **DERIVED on D1** (λ > 0). **REFUTED-ZERO** on the literal class; **OPEN** with subluminal photons. Count OPEN. [S26 reading] The photon and Dirac edges of the R18-5 and R18-9 roots have not been checked against the charge rows | P73: 3 per class / 7 per species, conditional. P101: ≤ 2 (upper bound) with a lattice-superluminal photon | None (`AX:114-130`); sizes `AX:189-190`. P101 gives up the gauge-field subluminality rule (`TESTS:5699`), not an axiom line |
| W2 | **Graviton production** | Six exclusions (X1; X-G; G-mix; auxiliary irreps; integer-law f-sum O(k⁴); dressed integer law). Z₂ clocks escape the f-sum bound (R17-1). Goldstone ≥ 4 branches; Theorem Z (R17-6, bounded). **Theorem Z₀: a statically visible gapless T₂ branch with a strict vector gap forces a pinch point in every f-sum class (R18-1, uniformly LR-local class)** | **DERIVED** (six exclusions + three bounded Z₂ obstructions: G, Z, Z₀). **Production OPEN.** Static window: screening at finite fugacity OPEN (`vR18-1:9`); [ref, R18-10 OPEN] dipole conservation on the moves buys no pinch at βU ≤ 2.5 (not a proof that every dipole-conserving ensemble screens) | P-N1 (= P41/P49/P71), a supplied CCR graviton. The Z₂ route (no production shown): P110 + P112 + P113 + P96; if the charge-free sector is used, P130 | P-N1: Qubit `AX:45-53` (`:47`). P110: `AX:47` presentation, `AX:57-61`. P112: `AX:37-41`. P113: `AX:82-90`. P96, P130: Admissibility dynamics (`AX:57-61`, `AX:114-123`) |
| W3 | **Graviton–matter cone** (bare cone, prescription-scoped) | Ξ < 0 on 𝒰₀ (R14-3) and B″ (R16-3). Universal negativity REFUTED (Z1). M non-local (Lemma M). U + E1: one K₆ off-axis condition (R17-4). Theorem F on the conditioned fast face (R17-10) | DERIVED in 𝒰₀ ∪ B″; REFUTED as universal. K₆ jointly with axis zeros: OPEN on 𝒮. [worker, R18-9] UD off-axis: face2 ≠ T₂g, a further condition; VW off-axis undefined. R18-13 [pending]. Physical: OPEN (W15) | P87 on U + P122 + law data P129 (VW stencils), P133 (Dirac pair block), P134 (Dirac O(q²) placement) [worker for P134]. M excluded (P123) | Shapes: none (`AX:116-123`). Vertex data: `AX:187` |
| W4 | **Shear** (supplied zero-point vacuum) | μ_E zero per mass on G_w (R14-3). Fermion loops opposite in sign (R16-13). **μ_T2: shape-zeroable on D1, one tuning (R17-13 ZEROED); not sign-definite.** **SM counts on conserved vertices: μ_E zeroed jointly with the axis rows with 3 tunings, signed stencil (R18-5, conditional)** | Not a wall in the empty vacuum. Otherwise: μ_E and μ_T2 each one row. **Four rows jointly at SM counts:** [worker, R18-9; referee running] FOUR-ROW-ZERO on the letter, 4 tunings + a photon window (`TESTS:7044-7059`) | [worker] R18-9's root: P109 (the Dirac edge on the μ_T2 zero curve) + shapes + P129 (signed) + P147 (photon window). Fallback if vR18-9 fails it: P100 or P109's 8-component option | P100: none / `AX:47` / `AX:184-187`. P109: none (tuning) or `AX:47` (8-component) |
| W5 | **Lattice-scale superluminality** | Lemma V; R14-1 repair; Lemma V1 (R16-13). Photon rule load-bearing (R16-10) | DERIVED (cause) and repaired for matter (unchanged) | P61 | `AX:57` |
| W6 | **BF photon multiplet** | Physically non-local in 𝓔 (R13-4(i)) | DERIVED in 𝓔 (unchanged) | P60 | Dynamics downstream; `AX:57` under a range reading |
| W7 | **Off-box gravity tail** | 1/r² kernel, box-inert (R16-8). T3/J3 weak closure (R16-12). B3 presentation-dependent (R16-12). Bulk term ≅ inverse of a linearized-GR Coulomb dressing (R17-2). **The complete improved generators fail the asymptotic algebra by Q_D at degree 2; no completion beginning at degree 3 cancels it (R18-8, ANOMALY)**; F(Q_D) at degree 3 conditional | **DERIVED as a boundary anomaly** in the standard Regge–Teitelboim phase space with free current-aligned S/G matter. **OPEN:** the singular dressing's boundary domain (F(Q_D)); the world-line presentation; the relic population; the readout of √(E² − P²) | **P141** (accept the anomaly) or **P142** (an initial-state condition: no edge quanta). P90 (SLAC matter) closes degree 2 off the face [worker]. P116/P118 carried; P117 → P141 only within Corollary N's narrow class [worker] | P141: `AX:57-61` (matter law), `AX:82-83`, `AX:187`. P142: none (an initial-state condition; formation downstream `AX:182-185`). P90: `AX:57-61`, `AX:187` |
| W8 | **Set A, covariant** | 𝒰 no-go (R12-4); E1 gain (R13-6); E2 drag (R14-2); spin-2 (R15-2); TT memory (R16-4); α₁ = α₂ = 0, γ = 1 (R16-14). Set A part of the joint bridge OPEN (R18-6). **E1 + N_c CONSTRUCTED through O(G²) in the weak-field harmonic static/quasi-static scope; R16-14's unprojected N non-conserving; N̄ not a linear channel (R18-7)** | DERIVED walls; E1 CONSTRUCTED in scope; E2 OPEN. **OPEN:** the gauge-invariant time-dependent noise, the Poisson-gauge kernel, premise (iii) beyond the static scalar channel. [worker, R18-11] At the gauge-independent insertion a = 2: a NOISE-OVERSHOOT candidate (×1.17–1e19 ρ_Λ) | E1: P65 + P76 + P88 (extended) + P107 made concrete as N_c: + **P138** (Π; causal, not spatially local) + **P139** (gauge) + **P140** (insertion weight a) [ref, in scope]. E2: P66 + P107 + an unbuilt sink (P137 is its set-A analogue). [worker] At a = 2: P145 + P146 + P-r15c (the γ-trade, now necessary) | `AX:185-186`; `AX:92-94` (P88); `AX:82-83`, `AX:187` (P107, P138–P140) |
| W9 | **Λ, fixed grid** | V1 tadpoles (R11-3). Tadpole strictly positive on 𝒮 (R17-4). Under (S), the enthalpy ρ₀+p₀ remains (R17-7). **(d-i) CONSISTENT in 𝒟 (R17-11): exact cancellation, no signalling, conditional bookkeeping** | DERIVED (unchanged). The universal (d-ii) no-go fails (`vR17-11:36`) | P51. Or under (S): (d-i) = P70(d-i) with P52 as receiver (a model postulate inside H-imp), P68's congruence and P128; or P70(d-ii) (pairing or ≥ 2 tunings per species) | `AX:187`; `AX:47` (pairing); `AX:37` (P52); `AX:189-190` |
| W10 | **Λ, site creation + P-T** | Bounded obstruction (R17-3). (S) consistent and number-free (R17-3), conditionally viable (R17-7). **P93 test OPEN: SM-only needs M_t ≤ 170.88 GeV; tension 1.48–3.09σ; lattice cannot stabilize in the H-EFT class; singlet or n5 ≥ 2 5-plets can (R18-2)** | DERIVED: without an added principle, no non-signalling route avoids a stipulated constant. OPEN: (S) with its conditions | P92 = (S) + P93 (either M_t ≤ 170.9 GeV, or **P131**/**P132** content) + (d-i) + R-label records (P4). Alternative P125 | `AX:187`; `AX:116-130`; `AX:94` (reading); `AX:79-83`; `AX:37` (P52). P131/P132: content, no axiom line (P132 needs chirally protected lattice fermions) |
| W11 | **Set C count** | R13-8; R16-2; R16-3; R17-4 (8/12 + CC); μ_T2 row (R16-13); μ_T2 shape-zeroable (R17-13); **conserved-vertex SM three-row root (R18-5, conditional)** | **OPEN.** Four-row joint point: [worker, R18-9] FOUR-ROW-ZERO on the letter, referee running. Off-axis rows unpaid (UD face2 ≠ T₂g [worker]); R18-13 [pending]; K₆/μ_E certificates OPEN | P72 refined by P73, P87, P122, P100, P109, P51 (0 numbers under (d-i)), P129, P133, P134, P147 | None (tunings); vertex data `AX:187` |
| W12 | **Matter on the box** (linear gravity) | R11-4 PASS WITH SCOPE (unchanged) | No wall at linear order | P56 | Unchanged |
| W13 | **Set B** | R10-2 (unchanged) | DERIVED | Give up RP, or whole-zone SLAC | Unchanged |
| W14 | **Λ, set A q-charge** | μ fixed to 2.1e-55 (R10-4) (unchanged) | Minimal realization excluded; OPEN beyond | P54 | Unchanged |
| W15 | **Translation Ward wall** (GW170817 as a gauge-invariant test) | T_pf single band (R16-5); EXCLUDED-MB (R17-5); Lemma N, MIX-1/2, FD, Theorem W (R17-8). **EXCLUDED-CROSS: two-band analytic crossings incl. Weyl points (R18-4)** | **DERIVED** for free finite-band local analytic matter in every form tried. **OPEN:** continuous multi-shift mixing, N > 2 braiding, joint mixing + FD, interacting, non-symmetric, non-projectable | P90; P64; P124 | P90: `AX:57-61`, `AX:187`. P64: `AX:47`. P124: `AX:187`, `AX:116-123` |
| W16 | **Newtonian attraction, sign-free finite slots** | Theorem D (R16-7) (unchanged) | DERIVED in the stoquastic conserving class | P97 | None; a source bridge is `AX:187` |
| W17 | **Post-Newtonian β from records** | A metric linear in matter records: β = 0 or ½; Mercury excludes both (R16-14). With Π, β = γ = 1 at O(G²) (R18-7). [worker, R18-7] Linear in the LL density variable: β = 3 | **DERIVED** for the literal linear completions | P107, made concrete (set A) as N_c with P138 [ref, in scope]; in C-box-E as P135 (N_red) [ref, conditional] | `AX:82-83`; `AX:187` |
| **W18 (new)** | **One source bridge: literal N with (d-i)** | Literal N (raw total matter-plus-vacuum stress + gravitational self-stress) with nontrivial (d-i): Bianchi forces Q = 0, hence W = 0 on any connected expanding slice (R18-6, `vR18-6:5`) | **DERIVED** (JOINT-CONFLICT) in class 𝒟, connected expanding slices, W ≠ 0. **OPEN:** the quantum J2 step; full quantum-gravity completion | **P135** (N_red: three clauses (S) + (d-i) + N_red, zero numbers, exact classical GR) [ref, conditional]; quantum: **P136** (J2) | P135: `AX:82-83`, `AX:187`. P136: `AX:47` (supplied sector), `AX:187` |
| **W19 (new)** | **Conserved, covariant TT vertices** | Lemma F (forward Ward value, necessary O(q)) excludes VU and VM's E_g row; Lemma C excludes VM's placement (R17-12). V0 fails Lemma F; Lemma M′ (spinor faces allowed) (R18-5). M non-local (Lemma M, R17-4) | **DERIVED** in R13-5's symmetric universal-energy W1 class at O(q): VU, VM, V0 and M excluded. **OPEN:** exact W1 completion of any vertex; uniqueness outside 𝔇 and outside the Maxwell-product tie | Surviving vertices U, UD, VW, with law data **P129** (VW stencils, signed allowed), **P133** (Dirac pair block / family 𝔇), **P134** (Dirac O(q²) placement) [worker] | `AX:187` (vertex data); `AX:114-130` (dynamics); `AX:57-58` (covariance, as Lemma M uses it) |

**[S26 reading] The shape of the map.**
- **Changed since S23:**
  - W2 gained a third bounded Z₂ obstruction (Z₀).
  - W4 lost its "separate knob" status for μ_T2.
  - W15 lost the crossing-band hole.
  - Two new walls are refereed: W18 (literal N vs (d-i)) and W19 (vertex conservation).
  - W7 is now DERIVED as a boundary anomaly (vR18-8, read from `SP/`), and W8's E1 route has a refereed construction in scope (vR18-7, `TESTS:7020-7027`). W8 also has a worker candidate wall: the record noise overshoots at the gauge-independent insertion (R18-11).
- **Still OPEN because a construction is unbuilt:**
  - W2: a pinch-point phase, then a light-like branch;
  - W7: the singular dressing's boundary domain (F(Q_D)), the world-line presentation, the relic population;
  - W8: the noise budget at a = 2 (R18-11's overshoot candidate, referee running; R19-2 for FRW);
  - W11: the off-axis rows (R18-13), and the referee of R18-9's four-row point;
  - W15: non-analytic and N > 2 routes;
  - W18: J2.
- **Where the axiom texts bear directly.** Unchanged in kind from S23:
  - Qubit (`AX:47`): W2 through the Z₂ reading;
  - Record readout (`AX:82-90`): W2, W7, W8, W17, W18;
  - "A law privileges no states" (`AX:94`): W10, through (S); W8, through P88 and P146's pre-loaded-energy reading;
  - everything else ends at the source/action gate (`AX:187`).
- **New in kind:** W19 is a wall made by the campaign's own Ward requirement (R13-5's W1 hypotheses), not by an axiom line. Its payments are vertex law data, which the axioms leave to the source/action gate (`AX:187`).

---

## 3. Price ledger delta since S23 (P129 onward; named only, none adopted)

S23 ended at P128 (`S23:552`). A grep of `TESTS`, `PRICE_NOTE`, `SUMMARY` and the round-17/18 reports and verdicts finds no use of P129 or higher.

### 3.1 Label collisions, resolved; count-once notes

| Worker label | Item | Meaning | S-number |
|---|---|---|---|
| P-K6′ | R17-10 | any shape solution of the K₆ row needs a finite fraction of slow-slope structure | **P122 refined** (no new number). The referee confirms only local persistence around realizable fast skeletons (`vR17-10:37`); the "finite fraction" form is [worker] |
| P-vac′, P-r1711a/b/c | R17-11 | (d-i); receiver; congruence; non-Lagrangian partner | **= P70(d-i), P52/P53, P68's hypothesis, P128** (as S23). Now refereed with corrections (§3.2) |
| P-R17-12a | R17-12 | the vector stress must have W1-correct forward values | **a correction, no price** (it excludes VU and VM's E_g; P126 status change) |
| P-R17-12b | R17-12 | three symmetric z-placement stencils (P_T, P_E^E, P_E^B) as law data; W1-invisible | **P129**. Refines P-R17-9b (= P127) and P-TTV₂ (= P63(iii)). R18-5 uses it with **signed** weights |
| P-R17-12c | R17-12 | keeping VM's one-sided placement: a graviton with h_xy at z + ½, or a non-covariant coupling | **= P127**, restated (count once). Not payable with R9-9's graviton under covariance |
| P-R17-13a | R17-13 | μ_T2 as a shape row: one Dirac-edge tuning per Wilson-Dirac edge | **= P109**, refined (no new number) |
| P-R17-13b | R17-13 | the conflict price at SM counts: a non-shape shear knob, Clifford-flat fermions, wider families, or weak-Wilson light doublers | **a menu, not a new price:** = P100 ∪ P109's 8-component option. "Wider families" is search scope. The light-doubler corner is excluded by R9-1 |
| P-r18-1a | R18-1 | a non-local or composite move set that unfreezes the charge-free sector | **P130** |
| (RK bridge) | R18-1 | equal-time S read as "static response" through the RK identity | **a registered setting bridge, not numbered** (`TESTS:6438`; `rR18-1:229`). It must be priced if a static result is ever used as evidence for production |
| P93 (sharpened) | R18-2 | SM-only: M_t(pole) ≤ 170.88 GeV, or new content below about 1.8e11 GeV | **= P93** (status change) |
| P-r182a | R18-2 | real singlet with Higgs portal and VEV; one unprotected scalar-mass tuning per species | **P131** |
| P-r182b | R18-2 | n5 ≥ 2 vector-like Dirac 5-plets, chirally protected | **P132** |
| (none) | R18-4 | no new price | P64, P90, P124 unchanged |
| P-R18-5a | R18-5 | the Dirac stress must have Lemma-F forward values | **a correction, no price** (P108's V0 half withdrawn) |
| P-R18-5b | R18-5 | the Dirac q = 0 pair block as law datum; restriction to 𝔇 (forcing UD) a stipulation | **P133** |
| P-R18-5c | R18-5 | the Dirac O(q²) placement (midpoint vs leg average) | **P134** [worker; up to about 10% per field on some laws] |
| P-r186a (J1) | R18-6 | N stated on the gravitating stress, i.e. N_red | **P135**. The worker called it "a rewording of P107"; the referee rules it a new completion (`vR18-6:5`) |
| P-r186b (J2) | R18-6 | (i) the supplied graviton is GR's self-coupled field; (ii) a quantum gravity sector is part of the H that defines e₀ | **P136**. (i) rides on P-N1 and W7's degree 3; (ii) OPEN (`vR18-6:7`) |
| P-r186c | R18-6 | set A: the record-production sector carries a conserved stress supplying the noise injection | **P137** [worker, suggested]. The set-A analogue of E2's missing sink |
| P-r18-7a | R18-7 | causal conserving projection Π | **P138** [ref, in scope: causal and conserving, not spatially local; `vR18-7:3`] |
| P-r18-7b | R18-7 | harmonic gauge of the O(G²) readout (conflicts with P-r15b) | **P139** [ref: the Poisson-gauge metric kernel is not preserved; `vR18-7:22-24`] |
| P-r18-7c | R18-7 | noise insertion weight a (one number) | **P140** [ref, scoped to the static homogeneous scalar channel; `vR18-7:20`] |
| P88 extension | R18-7 | the residual harmonic gauge modes' free data are zero at t₀ | **= P88**, extended (no new number) [ref, as a hypothesis of the construction; `vR18-7:26`] |
| P-W7anom | R18-8 | accept the asymptotic Poincaré anomaly | **P141** [ref, retained with corrected leading-order wording; `vR18-8:23`] |
| P-W7edge0 | R18-8 | physical states carry no edge quanta | **P142** [ref, narrowed: an initial-state/domain condition, not a derived selection rule; `vR18-8:23`] |
| P-W7bdy | R17-2 → R18-8 | boundary cross terms | **= P117**; [worker] its first branch is excluded at degree 2 and it reduces to P141, but only within Corollary N's narrow class (`vR18-8:15`) |
| P-pf1 | R18-8 | SLAC/sawtooth matter closes the degree-2 asymptotic algebra off the face | **= P90** (count once) |
| P-r18-10a | R18-10 | the γ-dipole conserved by the moves ≡ six conserved label totals | **P143** [ref for the identity, `vR18-10:3`]. Buys nothing static in the tested couplings (`vR18-10:7,15`; `rR18-10:250`) |
| P-r18-10b | R18-10 | 3L planar diagonal-label laws, which come with R18-1's patterns plus the dipole filter | **P144** [ref, `vR18-10:9`]. Fragmentation; 3(L − 1) independent invariants beyond the totals; no vector-channel effect (`rR18-10:251`) |
| P-r18-10c | R18-10 | planar laws for every row slot plus a prepared uniform sector (a stress test) | **named, not proposed; not numbered**. It needs a privileged state (`AX:94`) and only fakes axis pinches (`rR18-10:252`) |
| P-r1811a | R18-11 | the record is the conserved tensor density √−g T^{μν} (a = 2) | **P145** [worker]. Replaces P140's a = 4; makes P139 immaterial for the mean at O(G·noise²) (`rR18-11:233`) |
| P-r1811b | R18-11 | the S/V noise's energy history: (P) zero homogeneous energy at t₀ (default under P88), or (U) a pre-loaded datum | **P146** [worker]. (U) raises the `AX:94` privileged-state question (`rR18-11:234`) |
| P-r15c | R15-2 → R18-11 | the γ-trade (under-recorded S/V channels) | **carried, no new number**. [worker] Necessary at a = 2: γ_{S,V} ≤ ρ_Λ/(4u₁) (`rR18-11:235`) |
| P-R18-9a | R18-9 | the photon window: the photon edge in a narrow near-linear range (γG_w, b_γ ≈ 2.936–2.947) | **P147** [worker, suggested]. A law datum with an open condition; it may count as a fifth tuning (`rR18-9:307-310`) |
| P-R18-9b | R18-9 | the UD off-axis rows (face2 ≢ T₂g for UD) | **= P122 extended to fermions** (a bill row, not a new price; count once with the off-axis row) (`rR18-9:311-313`) |

**Spelling hazards.**
- R18-2 writes P-r182a/b and R18-6 writes P-r186a/b/c (no hyphen), while R18-1 writes P-r18-1a and R18-7 writes P-r18-7a/b/c (hyphen).
  - **"P-r186c" (P137, set A meter stress) and "P-r18-7c" (P140, the insertion weight) are easy to confuse, and both concern set A's noise.**
  - "P-r182a" (P131, singlet) reads like "P-r18-2a", which does not exist.
- R18-5 and R17-12/13 use uppercase P-R…; R18-8 uses P-W7….
- S23's hazard "P-r1711a" (R17-11) vs "P-r17-1a" (R17-1) still applies. **R18-11 did add "P-r1811a"** (P145, the a = 2 insertion), which collides visually with "P-r18-1a" (P130, R18-1's move set). R18-10 writes "P-r18-10a" (P143), which collides with both.
- **The wrap-up should use only S-numbers.**

**Count once [S26 reading].**
- **The set-A noise budget.** P137 (a conserved meter stress for the injection), P140/P145 (where the noise enters the source: a = 4 or a = 2), P146 (the noise's energy history) and premise (iii) (R15-2) are views of one quantity: the active gravitating density of the record noise. [worker, R18-11] At a = 2 it is −4u₁ (U) or at most −u₁ (P), so premise (iii) is quantitatively live there. Keep them as separate prices until a referee rules on R18-11.
- **The grid enthalpy** (carried from S23): P51 = P-Tad = P70's uniform part = R17-7's enthalpy residual. vR17-11 confirms "the same operator direction … counted once for the same content and vertex" (`vR17-11:39`).
- **Vertex law data.** P63(iii) (scalar E1/E2 extension), P129 (vector stencils), P133 (Dirac pair block) and P134 (Dirac placement) are four instances of one unfixed object: the graviton–matter vertex beyond the forward Ward value. R17-12 names the principle that could fix them all: derivation from one lattice action √g F² (and its Dirac analogue) with a stated metric placement, not attempted (`rR17-12:279`).

**Theorem-name collisions** (new since S23; cite as "item + name").
- "Lemma F": R13-3, R16-2, R16-8, R17-5, and now **R17-12 (forward Ward value)**. "Theorem F": R17-10.
- "Lemma C": R14-5, and **R17-12 (covariance)**.
- "Lemma X": R17-7 (records), **R17-12 (T₂g vertex fixed)**. "Lemmas X1/X2": **R18-4**; these also collide with the W2 exclusion "X1" and C3's lanes X1/X2.
- "Lemma S": R15-1 (signalling), **R17-13 (mirror μ_T2)**; "Lemma S0" (R18-4); "Lemma S∞" (R18-8).
- "Lemma D": R13-6, R16-8, R17-2, **R18-5 (UD unique in 𝔇)**; "Lemma D₀" (R18-5).
- "Lemma M′": R18-5 (spinor faces), beside "Lemma M" (R16-4, R17-3, R17-4).
- "Theorem Z₀": R18-1, beside "Theorem Z" (R16-6, R17-6).
- "Theorem W" (R16-1, R17-8); "Theorem WX" (R18-4).
- "Corollary N/N′" (R18-8), beside "Lemma N" (R15-3, R17-8), "completion N", N_red, N̄, N_c. **"N" is now the most overloaded letter in the campaign.**
- "Lemma T" (R18-8), beside "Theorem T" (R9-9, R17-3).
- "Theorem A", "Theorem A3" (R18-8). "Lemma I" (R17-12). "Lemma RB-X" (R18-4), beside "Lemma RB" (R17-5).

### 3.2 Status changes to earlier prices

- **P52** (site creation; receiver for (d-i)). Valid as a receiver inside H-imp, but "not established as a consequence of the lattice axioms": the insertion law and any equation conjugate to site number are unbuilt (`vR17-11:22-23`).
- **P63(iii)** (vertex as law datum). Now has vector and Dirac instances (P129, P133, P134).
- **P70 (d-i)** [now ref]. Consistent, covariant and non-signalling in 𝒟, on shell, one-point (`vR17-11:44-45`). The bill reduction is conditional bookkeeping (`vR17-11:39`). **P70 (d-ii)**: S23's "still needs W = 0" was overclaimed; for nonuniform W, D_iW + Wa_i = 0 is satisfiable locally with W ≠ 0 (`vR17-11:36`).
- **P88** (initial TT datum). Extended to residual harmonic gauge modes, as a hypothesis of R18-7's construction [ref, `vR18-7:26`].
- **P92 = (S).** Unchanged in status (consistent, number-free, unforced). Two refinements:
  - [ref, `vR18-2:15`] the true-minimum condition follows only after identifying the observed vacuum source with the energy above the law's ground;
  - [ref, `vR18-6:13`] with (d-i) and N_red it is part of a three-clause, zero-number classical bridge.
- **P93** (late-vacuum stability). Sharpened [ref, `vR18-2:5-7`]: SM-only needs M_t(pole) ≤ 170.88 GeV at two loops (Buttazzo fit 170.997); the recalled inputs give 1.48–3.09σ, not a robust conflict. Otherwise new content below about 1.8e11 GeV (P131 or P132).
- **P96** (emergent constraint, not dressing-connected). Z₀ [ref, bounded] makes a pinch point necessary in its class. Finite-fugacity screening is OPEN (`vR18-1:9`). P130 is its charge-free-sector form. [ref, R18-10, in the tested couplings] A conservation law on the moves of an RK ensemble cannot replace exact charge suppression (`rR18-10:254`).
- **P100** (non-shape shear knob). Becomes the fallback for the four-row point if R18-9 fails.
- **P107** (completion N).
  - [ref, `vR18-6:5`] Literal N conflicts with (d-i) when W ≠ 0 (W18). In C-box-E use P135.
  - [ref, R18-7] In set A, R16-14's unprojected N is genuinely non-conserving (`vR18-7:5-9`). The concrete form N_c = P107 + P138 + P139 + P140 + P88 (extended) is CONSTRUCTED in the weak-field harmonic static/quasi-static scope (`vR18-7:26`).
  - [ref] Its alternative N̄ is not a linear quantum channel, hence not CP in the standard sense (`vR18-7:11`).
- **P108** (V0 + SF). **The V0 half is withdrawn:** V0 fails the forward Ward value (`vR18-5:3`). The SF half (P-R16-13a) stays a stipulation. μ_E and μ_T2 depend only on SF (`vR17-13:11`).
- **P109** (μ_T2). Refereed as a shape row: one continuous Dirac-edge tuning per edge (`vR17-13:13,17`). The 8-component option (`AX:47`) remains the non-tuning alternative.
- **P112** (shift action). Needed for the RK charge penalty to be cubic-covariant (24/24 vs 6/24, `vR18-1:5`).
- **P117** (boundary charges). [worker, R18-8] reduces to P141, within Corollary N's narrow class (`vR18-8:15`).
- **P139, P140** (set A gauge and insertion). [worker, R18-11] The a = 4 zero holds only for static ρ-only noise in reading (U). a = 2 (P145) is the unique readout-gauge-independent insertion, and at a = 2 P139 is immaterial for the mean (`rR18-11:142,233,245-251`).
- **P-r15c** (the γ-trade, R15-2). [worker, R18-11] Necessary, not optional, at a = 2 (`rR18-11:235`).
- **P122** (K₆). Theorem F on the conditioned fast face [ref, `vR17-10:53`], with local persistence. Not CERTIFIED-CONFLICT.
- **P126** (VU vertex). **Withdrawn as a conserved vertex:** VU fails Lemma F (`vR17-12:5-11`). Its numbers belong to a non-conserved vertex.
- **P127** (VM placement). **Not payable with R9-9's graviton under covariance:** Lemma C (`vR17-12:13`), and VM's E_g row fails Lemma F. Restated as P-R17-12c.
- **P128** (non-Lagrangian partner). Confirmed only against a single ultralocal P(X). Derivative, multiplier, discrete and multi-field actions are open (`vR17-11:35`).
- **P64, P90, P124.** Unchanged for W15 (`rR18-4:307-308`). P90 also closes W7's degree-2 algebra off the zone face [worker, `rR18-8:180`].

### 3.3 New prices

| # | Price (named only) | Axiom text touched | Set | What the record says it buys or costs |
|---|---|---|---|---|
| P129 | **VW placement stencils** (R17-12 P-R17-12b): three normalized symmetric z-stencils (P_T, P_E^E, P_E^B) as law data; signed weights allowed in R18-5 (λ = 0.0045; weights 1.1227446, −0.1227446) | `AX:187` (vertex datum); dynamics `AX:114-130` | C-box | W1-invisible: they differ by identically conserved superpotentials (`vR17-12:15`). Each moves its TT row linearly. With signed weights, one of them is the third tuning of R18-5's SM root (`vR18-5:16`). `rR17-12:279`; `rR18-5:311` |
| P130 | **A move set that unfreezes the charge-free sector** (R18-1 P-r18-1a): non-local or composite moves at βU = ∞ | Admissibility dynamics (`AX:57-61`, `AX:114-123`) | All grid | The registered moves are frozen there (`vR18-1:5`). Minimal integer-invariant moves have weight ≥ 20 in tested boxes; that is the integer-law sector R16-7/R16-11 cap [worker]. `rR18-1:231` |
| P131 | **Higgs-portal singlet** (R18-2 P-r182a) | Content; no axiom line | C, C-box (any option with (S)) | Stabilizes the EW vacuum over O(1) coupling windows, m_S < 3.17e10 GeV (referee-corrected), with **one unprotected scalar-mass tuning per species** (`vR18-2:11`). `rR18-2:278` |
| P132 | **Vector-like Dirac 5-plets, n5 ≥ 2** (R18-2 P-r182b), no Yukawa | Content; needs chirally protected lattice fermions (reading) | C, C-box | Stabilizes with 0 tunings and one technically natural hierarchy. Mass ceilings not precision results; collider and relic costs RECALLED (`vR18-2:13`). `rR18-2:279` |
| P133 | **The Dirac pair block as law datum** (R18-5 P-R18-5b): restricting to the strain-flow family 𝔇, which forces UD | `AX:187`; `AX:114-130` | C-box | Lemma F fixes only the band-diagonal contraction. Outside 𝔇 the pair block is free and gives very different Ξ (`vR18-5:7`; `rR18-5:305-308`) |
| P134 | **The Dirac O(q²) placement** (R18-5 P-R18-5c): midpoint vs leg-average k_z dependence of UD | `AX:187` | C-box | [worker] Moves Ξ by up to about 10% per field on some laws. The referee lists the O(q²) placement as not derived (`vR18-5:22`). `rR18-5:309` |
| P135 | **N_red**: the metric is sourced by T_m − (V − e₀)g plus gravity's own stress (R18-6 P-r186a) | `AX:82-83` (readout); `AX:187` (source) | C-box-E | With (S) and (d-i): exact classical GR, TOV without W, β = γ = 1, Λ̃ = 0 under P93, no Lemma-S channel; three clauses, zero numbers. **A new completion, not a wording fix** (`vR18-6:5,11,13`). `rR18-6:175` |
| P136 | **J2** (R18-6 P-r186b): (i) the supplied graviton is GR's self-coupled field; (ii) a quantum gravity sector lies inside the H that defines e₀ | `AX:47` (supplied sector, as P-N1); `AX:187` | C-box-E | Classical branch sound. Quantum claim OPEN: isotropy needs cubic invariance; the virial identification covers only free gauge-fixed TT modes (`vR18-6:7`). `rR18-6:176` |
| P137 | **A conserved meter-sector stress for set A's noise injection** (R18-6 P-r186c) | `AX:185` (record production); `AX:187` | A | [worker, suggested] The set-A analogue of E2's missing sink. A meter-sector receiver is not excluded (`refR18-6:34`). Possibly the same object as P140 and premise (iii) (§3.1). `rR18-6:177` |
| P138 | **Causal conserving projection Π** (R18-7 P-r18-7a) | `AX:187` | A (E1) | [ref, in scope; `vR18-7:3,26`] Without it N does not close at O(G²). Causal and conserving, but not spatially local (algebraic tails). Non-unique up to a conserved tensor; it can renormalize the mass at O(G²)/r but cannot change the M²/r² PPN coefficient (`vR18-7:18`). `rR18-7:247` |
| P139 | **Harmonic gauge for the O(G²) readout** (R18-7 P-r18-7b) | `AX:82-83` | A (E1) | [ref] Conflicts with P-r15b: the Poisson-gauge metric-component kernel is not preserved, and there is no gauge-invariant time-dependent O(G²) noise result (`vR18-7:22-24`). [worker, R18-11] built the Poisson-gauge law on Minkowski; at a = 2 the gauge is immaterial for the mean. `rR18-7:248` |
| P140 | **Noise insertion weight a** (R18-7 P-r18-7c): one number | `AX:82-83`; `AX:187` | A (E1) | [ref, scoped] Static homogeneous scalar ρ-noise: energy density (2a − 7)\|u₁\|, active density (2a − 8)\|u₁\|, zero at a = 4 (the unchanged meter). It does not cancel the +\|u₁\| LL energy density or settle the other channels (`vR18-7:20`). `rR18-7:54,249` |
| P141 | **Accept the asymptotic Poincaré anomaly** (R18-8 P-W7anom): {K_b, P_c} = δ_bc H + Q_D,cb at leading order (F(Q_D) at degree 3, conditional) | `AX:57-61` (matter law); `AX:82-83`; `AX:187` | C-box | [ref, retained with corrected wording; `vR18-8:23,25`] Consistency of the bulk constraint algebra with the asymptotic charges. Its signature, √(E² − P²) varying with velocity, is a frame-dependent translation-charge functional, observable only under the ADM/source/readout bridge (`vR18-8:19`). `rR18-8:178` |
| P142 | **No edge quanta in the initial state** (R18-8 P-W7edge0) | None (an initial-state condition); formation rules downstream (`AX:182-185`) | C-box | [ref, narrowed] An initial-state/domain condition preserved by the number-conserving model; not a derived state-selection rule (`vR18-8:23`; `refR18-8:171-176`). Broken by pair creation or interactions. `rR18-8:179` |
| P143 | **Dipole conservation on the moves** (R18-10 P-r18-10a): equivalent to six conserved label totals | Admissibility (`AX:57-61`, `AX:116-123`): a conservation law on moves is new structure | All grid | [ref, `vR18-10:3,7`] Buys nothing static through βU ≤ 2.5: the fixed-dipole sector has R18-1's ξ. Costs slow (glassy) local dynamics at βU ≥ 2.5. `rR18-10:250` |
| P144 | **Planar diagonal-label laws** (R18-10 P-r18-10b): 3L frozen plane charges | As P143, plus subsystem structure on the Lattice (`AX:37-41`) | All grid | [ref, `vR18-10:9`] Fragmentation (511 classes for 1024 states at L = 2) and a frozen zz axis channel in a chosen class; no vector-channel effect. `rR18-10:251` |
| P145 | **The record as √−g T^{μν}** (R18-11 P-r1811a; insertion a = 2) | `AX:82-83`; `AX:187` | A (E1) | [worker] The unique readout-gauge-independent insertion in the three power families (Theorem G). At it, the noise's active density overshoots ρ_Λ over R15-2's whole window unless P-r15c is paid. `rR18-11:142,233` |
| P146 | **The S/V noise's energy history** (R18-11 P-r1811b): (P) zero homogeneous energy at t₀, or (U) a pre-loaded datum | `AX:92-95`; `AX:185` | A (E1) | [worker] (P) is the default under P88; (U) needs a privileged-state datum (`vR16-4:17`). `rR18-11:234` |
| P147 | **The photon window** (R18-9 P-R18-9a): the photon edge γG_w with b_γ ≈ 2.936–2.947 (at fw = 1, G_w scalars) | `AX:187`; dynamics `AX:114-130` | C-box | [worker, suggested; referee running] Needed for all four axial rows at SM counts; replaces R18-5's photon edge, which cannot carry the fourth row (`rR18-9:187-193,307-310`) |

**Named gaps, not prices.**
- No exact W1 completion exists for any vertex (U, UD, VW) (`vR17-12:15`; `vR18-5:22`).
- No lattice action derivation of the vertex law data (`rR17-12:279`).
- No FRW version of Π for set A (`rR18-11:271`). R18-11 built the Poisson-gauge law on Minkowski [worker].
- No microscopic site-creation law (`vR17-11:22-23`).

**[S26 reading] How the price structure shifted since S23.**
- **Vertices: from "pick a placement" to "pick law data after a Ward test".** Three vertices fell (VU, VM, V0). The survivors carry unfixed law data (P129, P133, P134). S23's P126 and P127 are withdrawn or restated.
- **Λ and β: one classical package.** P92 + P70(d-i) + P135 replace "(S) plus conditions plus a separate β completion". The package's open edges are P136 (quantum) and P93 (particle physics, where P131/P132 are the named content options).
- **Set A: three concrete stipulations replace one abstract one** [ref, in scope]: P107 becomes P138 + P139 + P140.
- **W7: a price where there was an open algebra** [ref]: P141, or P142 as an initial-state condition.
- **Set A's noise: from an unproved premise to a candidate wall** [worker, R18-11]. At the one gauge-independent insertion, the γ-trade (P-r15c) becomes necessary.
- **Nothing new is needed for W15.**

---

## 4. Owner decision memo (for Jon; supersedes S23 §4; options with prices; nothing adopted)

### 4.1 The question in one line [S26 reading]

On a slower-than-light grid, what has been computed can be made to agree with relativity at no fewer than nine tuned numbers plus the cosmological constant (plausibly nine to eleven). Each is held to 1e-13–1e-16, on vertices that now pass the campaign's own conservation test, but only with vertex details that nothing fixes. Classically, gravity's source can be stated in three added sentences with no number, and that reproduces Einstein's equations exactly; whether it survives quantum gravity is open. The graviton still cannot be produced from the axioms' qubits by any construction on record. Its window now has a proved static signature and no example.

### 4.2 Options (updated)

**Option A: continuum base, discreteness only in records.**
- *Buys:* exact Poincaré, one cone, no LV tunings. Newtonian records-as-metric VIABLE (R6-4).
- *Pays:*
  - a supplied graviton;
  - to go covariant with β = 1: E1 + N_c, i.e. P65 + P76 + P88 (extended) + P107 + **P138 (Π) + P139 (gauge) + P140 (insertion weight)** [ref, CONSTRUCTED in the weak-field harmonic static/quasi-static scope; `vR18-7:26`]; or E2 (P66 + P107 + an unbuilt sink, cf. P137);
  - Λ by (S) (P92). The matter vacuum then needs no (d-i), because a Poincaré-invariant vacuum has W = 0 [ref, `vR18-6:9`]. Or a q-charge (P54).
- *Open:* whether the record noise gravitates (premise (iii)). [ref, scoped] Its static scalar part is zero at a = 4 (`vR18-7:20`). [worker, R18-11] But a = 4 depends on the readout gauge once the noise varies in time. At the one gauge-independent insertion, a = 2, the noise's active density overshoots ρ_Λ across R15-2's window unless the S/V channels are under-recorded (P-r15c) (`rR18-11:27-43`). R19-2 drafts the FRW step.
- *New since S23:* the mean-field variant N̄ is not a linear quantum channel [ref, `vR18-7:11`], so it leaves the menu of CP laws.

**Option C: keep the four texts and tune.**
- *Buys:* no text changes.
- *Pays:* the bill of §1.6, at least 9 + CC per class (plausibly 9–11) on conserved vertices (U + UD + VW + E1), conditional bookkeeping; P51; a supplied graviton.
- *Open:* the four-row SM point ([worker, R18-9] FOUR-ROW-ZERO on the letter; referee running); the off-axis rows (UD face2 ≠ T₂g [worker]; R18-13 running); K₆ and μ_E certificates.

**Option C-box: Z³, a box-exact law, qubits in a sector.**
- *Buys:* as S17/S20/S23.
- *Pays:* S23's list, with these changes:
  - VU, VM and V0 are excluded (W19);
  - vertex law data P129, P133, P134, and the photon window P147 [worker];
  - μ_T2 as a shape tuning (P109).
- *Open:* W15 (now only non-analytic or N > 2 routes); W7's relic population, given the refereed anomaly (P141 or P142).

**Option C-box-E (new name, R18-6): C-box with site creation, √h fixed per site and the E-sector.**
- *Buys:* the three-clause classical source bridge, (S) + (d-i) + N_red: exact GR on T_m − (V − e₀)g, β = γ = 1, Λ̃ = 0 under P93, no faster-than-light channel, zero numbers [ref, conditional; `vR18-6:13`].
- *Pays:* P92, P70(d-i), **P135**, P52 (site creation, as a model postulate inside H-imp), P68's congruence, P128, and P93.
- *Open:* J2 (P136; `vR18-6:7`); everything Option C-box leaves open.

**Option C-box-S: C-box with boson–fermion pairing per cell.**
- *Buys:* as S23, plus the pairing route for the vacuum enthalpy.
- *Pays:* P46 plus one of P58–P60, and still P73.

**Cosmology overlay (any option).**
- Active CMC compensation: FAIL (R15-1).
- g ≡ 0 with a stipulated constant: a counterterm (R16-6).
- (S), C = E₀[H]: number-free, with P93 as its particle-physics condition (Q1).

### 4.3 Questions only Jon can answer

**Q1 (replaces S23 Q1). Gravity's source: will you add three sentences?**
- **What it is** [ref, `vR18-6:13`; `vR17-11:44-45`; `vR17-3:17`]. In C-box-E, three rules together give exactly Einstein's equations, sourced by ordinary matter plus "vacuum energy minus the lowest state's":
  1. **(S)** the law's lowest state weighs nothing (P92);
  2. **(d-i)** the grid vacuum's leftover pressure is handed to the site-making sector (P70(d-i), receiver P52);
  3. **N_red** the metric is sourced by matter plus the vacuum's energy above the lowest state, plus gravity's own stress (P135).
- **Three clauses, zero numbers.** The referee rules this consistent classically, but N_red is a **new completion**, not the earlier completion N. The literal "total stress, vacuum included" version **conflicts** with (d-i) wherever the vacuum enthalpy is nonzero on an expanding slice (`vR18-6:5`, W18).
- **What it predicts.**
  - Mercury right (β = γ = 1); zero leftover Λ if our vacuum is the lowest state; no faster-than-light channel.
  - **The Higgs vacuum must be the true minimum**, once the observed vacuum source is identified with our state's energy above the law's ground (`vR18-2:15`). With Standard-Model content only, that means **M_t(pole) ≤ 170.9 GeV** (`vR18-2:5`). The recalled measurements sit 1.5–3.1σ above it: suggestive, not decisive (`vR18-2:7`). Otherwise there must be new content below about 1e11 GeV. Two kinds work:
    - a singlet scalar (P131): one unprotected mass tuning per species;
    - two or more vector-like 5-plets (P132): no tuning.
  - The lattice itself cannot do it in the tested class (`vR18-2:9`).
- **What it does not yet cover.**
  - **Quantum gravity (P136, J2).** If gravity is quantum, its own zero-point must be part of "the lowest state". Then (S) removes its energy and (d-i) its pressure. The referee confirms this only for free gauge-fixed graviton modes; it is OPEN in general (`vR18-6:7`). R19-3 drafts the test.
  - **The receiver.** Site creation with fixed volume per site is a model postulate, not derived from the lattice axioms (`vR17-11:22-23`). The vacuum's Planck-sized inertia is exactly compensated, not absent (`vR17-11:28-29`).
- **Your questions:**
  - (i) Would you state (S), (d-i) and N_red as principles? Each is independent: dropping any one brings back a Planckian enthalpy, a free Λ counterterm, or β = 0 or ½ (`rR18-6:164-167`, worker; consistent with the refereed pieces).
  - (ii) Is "the law's lowest state" a privileged state under `AX:94` (carried; no referee ruled)?
  - (iii) For P93: would you rather bet on M_t ≤ 170.9 GeV, or add content (P131 or P132)?
  - (iv) Is site creation (P52) acceptable against `AX:37`'s fixed Z³?

**Q2 (updated). Set A's nonlinear source (P107 made concrete).**
- **Now known** [ref, R18-7, CONSTRUCTED in the weak-field harmonic static/quasi-static scope; `vR18-7:26`]:
  - completion N as first written is genuinely non-conserving at second order; a conserving projection Π (P138) is needed. Π is causal but not spatially local (`vR18-7:3,9`);
  - with Π, harmonic gauge (P139) and an insertion weight a (P140), set A's E1 gives Mercury right (β = γ = 1) and keeps the quantum instrument CP (`vR18-7:11,18`);
  - the mean-field variant N̄ is **not** a linear quantum channel, so not CP in the standard sense (`vR18-7:11`).
- **Open, and sharper** [worker, R18-11; not refereed]: for time-dependent noise the gauge is a physical choice. Only a = 2 (the record read as √−g T, P145) is gauge-independent, and there the record noise overshoots ρ_Λ by ×1.17 to ×1e19 across R15-2's window. The escapes are the γ-trade (P-r15c, now necessary) or a tuning to precision ρ_Λ/u₁. A suggested FRW twist: the noise may settle into a positive cosmological constant equal to ρ_Λ near ℓ ≈ 3.7 µm (R19-2 drafts the test).
- **Your questions:**
  - (i) Is a metric that is a nonlinear functional of records still "determined by record content alone" (`AX:82-83`)? (carried)
  - (ii) Which insertion do you intend: a = 4 (the meter unchanged; harmonic-gauge law data) or a = 2 (the record as √−g T; gauge-independent; P145)? [worker, R18-11] The a = 4 zero does not survive time dependence.
  - (iii) N̄ is refereed not CP in the standard sense (`vR18-7:11`). Drop it from the menu?

**Q3 (updated). The qubit window for the graviton.**
- **Now known** [ref]:
  - the Z₂-clock reading escapes the f-sum bound (R17-1);
  - a graviton with gapped vector/scalar partners that the readout can see must show a pinch point, **whatever its f-sum** (Z₀, R18-1, in a uniformly local class);
  - in the simplest local ensemble that penalizes the leftover charges, no pinch point was seen through βU = 4. Smaller penalties look screened; the strongest is not equilibrated; exact suppression freezes local dynamics (`vR18-1:9`). So whether finite fugacity always screens is OPEN.
- **Tried** [ref, R18-10 OPEN; `vR18-10:15`]: conserving the charges' dipole moment on the moves fixes only six global totals and does not prevent screening. A fracton-type constraint would have to be imposed on the states themselves, which is P96 again (`TESTS:6978-6984`; `vR18-10:15`). This does not prove that every dipole-conserving ensemble screens.
- **Not yet asked:** whether any such phase has a light-like (ω = ck) branch. R19-1 drafts it.
- **Your questions:**
  - (i) Is a Z₂-clock reading with a mod-2 conserved structure (P110) within Qubit plus Admissibility? (carried)
  - (ii) Is a readout nonlinear in records (P113/P114) acceptable? (carried)
  - (iii) If a pinch-point phase needs an exact local constraint imposed on the states (P96), is that within the admissibility rule (`AX:57-61`)?
  - (iv) The rotation action on the possibility domain (P112) is now needed even for the static test (`vR18-1:5`). Is that a Lattice choice you accept?

**Q4 (updated). GW170817 on a grid (W15).**
- Crossing bands, Weyl points included, are now excluded too [ref, R18-4].
- The menu is unchanged: P64 (tower), P90 (discontinuous symbol), P124 (non-canonical shift), non-analytic or N > 2 matter, interactions, or accepting a bare-cone (prescription-scoped) comparison.
- **Your question:** which of these, or the last? (carried)

**Q5 (replaces S23 Q5). The cone bill on conserved vertices (§1.6).**

| Item | Tunings |
|---|---|
| Charged-matter cones (per (spin, \|q\|) class) | 3 |
| Graviton axis cone + E_g shear (SM counts: 2 edge shapes + 1 VW stencil) | 3 |
| Off-axis TT (K₆ for scalars; ≥ 1 more for UD Dirac [worker]; VW undefined) | 1–2 or more (R18-13) |
| T₂g shear (one Dirac-edge shape; jointly zeroed at SM counts [worker, R18-9]) | 1 (+1 if the photon window counts) |
| Vacuum tadpole (ρ + p) | 1, or 0 numbers under (d-i) |
| Cosmological constant | 1, or 0 numbers under (S) |
| **Total** | **9 + CC per class as a floor** (13 + CC per species); plausibly 9–11 + CC once the photon window and the fermion off-axis rows are counted [S26 reading on worker R18-9]; 8 numbers + 2 rules at the floor with (S) and (d-i) |

- **What changed** [ref]:
  - the campaign's conservation test removed both earlier photon placements (VU, VM) and the Dirac vertex used since round 16 (V0) (`vR17-12:17`; `vR18-5:3`);
  - on the surviving vertices, SM content zeroes three rows with three tunings, **if the photon's placement stencil may have a negative weight** (`vR18-5:16-20`);
  - the earlier Dirac obstruction belonged to the discarded vertex (`vR18-5:7`).
- **Now, from a worker** (R18-9; referee running): all four axial rows vanish together at SM counts with 4 tunings and a narrow photon window. **Still open:** the off-axis rows (UD face2 ≠ T₂g; R18-13 running).
- **Your questions:**
  1. Is about nine numbers at this precision acceptable for keeping all four texts? (carried)
  2. Per class (3) or per species (7)? (carried)
  3. **New.** Vertex details beyond the conservation test (the photon stencils P129, the Dirac pair block P133, the Dirac placement P134) are law data, and so, at SM counts, is the photon window P147 [worker, R18-9]. Would you choose them, or require them to come from one lattice action (not yet attempted, `rR17-12:279`)?
  4. **New.** Are signed (partly negative) stencil weights acceptable (`vR18-5:16-20`)? If not, the SM line is OPEN.
  5. For μ_T2: one edge-shape tuning (P109, refereed shape row), or 8-component fermions (`AX:47`)? (refined)
  6. Is lattice-scale superluminality excluded for the photon too (P101)? (carried)

**Q6 (carried). The initial gravitational-wave datum (P88).** Now also covers the residual harmonic gauge modes in set A [ref, as a hypothesis of R18-7's construction]. Tied to Q2.

**Q7 (carried). E1 or E2.** Observationally tied (R16-14). E1 now has a concrete second-order construction [ref, in scope], and a worker overshoot candidate at the gauge-independent insertion (R18-11); E2 still lacks a sink action (P137 is the set-A analogue).

**Q8 (new). The off-box tail at infinity (W7)** [ref, R18-8 ANOMALY; `vR18-8:25`; not yet recorded in `TESTS`].
- **Refereed.** On the grid, particles whose momentum sits at the zone edge make the total energy, momentum and boost charges seen from far away fail the Poincaré relations, by exactly those particles' defect charge. No completion of the gravity sector that starts at degree 3 can cancel it (`vR18-8:21,25`). That no boundary term repairs it is shown only for linear gauge-invariant metric functionals (`vR18-8:15`).
- **Observable.** For a body containing such quanta, the far-field combination √(E² − P²) depends on its speed and direction relative to the lattice. Since Poincaré closure fails, this is a frame-dependent charge combination, not an invariant mass; calling it observable assumes the ADM/source/readout bridge (`vR18-8:19`). Thermal populations make it tiny below about 1e18 GeV under stated assumptions. A relic population is not bounded by anything computed so far.
- **Options:**
  - (a) accept the anomaly (P141) and bound the relics (R18-12, running, `TESTS:6988-7019`);
  - (b) require that the initial state carry no edge quanta (P142). The referee reads this as an initial-state/domain condition, not a derived selection rule; number conservation keeps it, pair creation would not (`vR18-8:23`);
  - (c) SLAC-type matter (P90).
- **Your question:** (a), (b) or (c)?

**Q9 (carried; S23 Q8).** Edge-shape tuning; pairing per cell (`AX:47`); site creation (`AX:37`); a law that reads only changes in stress (`AX:94`); range (box tails, W7's 1/r², P90's 1/n tails); sector selection (P45).

### 4.4 Open in every option

- **Producing the graviton.** The static window needs a pinch point (Z₀). Screening at finite fugacity is OPEN; dipole conservation on the moves did not help (R18-10, refereed OPEN). A light-like branch is not addressed (R19-1).
- **Quantum gravity inside "the lowest state"** (J2, P136).
- **GW170817 as a gauge-invariant test on any grid** (W15): non-analytic and N > 2 routes.
- **W7's relic edge population**, and the readout bridge that makes the anomaly a measurement (R18-8 refereed; R18-12 running).
- **Set A's record-noise budget** at the gauge-independent insertion ([worker] R18-11; R19-2 drafted).
- **The full tuning count:** the four-row point, the vector/Dirac off-axis rows, the K₆ and μ_E certificates, and exact W1 completions of every vertex.
- **N ≥ 3 tails** (R11-6) and **the body quadrupole** (P56).

---

## 5. Dated corrections (this period; dated 2026-10-13)

| Correction | What it was | What it is now | Source |
|---|---|---|---|
| **V0 is not conserved** | R16-13's V0 Dirac TT vertex (Wilson mass uncoupled) used for every Dirac Ξ number from R16-13 through R17-12 (rR16-13 §3.3; R17-9's rows; R17-12's solves) | V0 fails the forward Ward value (+0.2654 where −0.2654 is required; O(1) off-box defects). Those numbers belong to a non-conserved vertex. The replacement UD is unique only within the stipulated family 𝔇. μ_E and μ_T2 are unaffected (they depend only on SF) | `TESTS:6779-6782,6964-6966`; `vR18-5:3,7`; `vR17-13:11` |
| **R16-13's birefringence obstruction belongs to V0** | "Dirac birefringence Ξ_T2g − Ξ_Eg ≥ +2.6e-3 per field on every Dirac law tested dominates" (`rR16-13:59,200,225`; `S23:202`); the premise of R17-9's VU conflict and of R18-3 | Under UD the birefringence spans −5.19e-4 to +2.40e-3. The sign obstruction is V0-prescription-specific, not a conserved-vertex theorem | `vR18-5:7` |
| **VU and VM are both excluded** | R17-9: "VU no SM zero; VM an SM zero with 3 tunings"; P126 (VU) and P127 (VM) as law data; S23 W4/W11/Q5 "half a cell over: yes" (`S23:84-86,690-694`) | VU fails Lemma F. VM's E_g row fails Lemma F, and its one-sided placement breaks C₂ covariance about R9-9's h_xy. R17-9's VM root is void as a conserved covariant vertex. The surviving family is VW, with free O(q²) stencils | `TESTS:6795-6801`; `vR17-12:5-19` |
| **R17-12's fixed reading** | Worker: OPEN, with a registration note (`rR17-12:288-293`) | FORCED-VU + FORCED-VM, both through their exclusion disjuncts, annotated NEITHER. A malformed-reading collision, not OPEN | `vR17-12:17` |
| R17-12 numbers | VU violation 0.25–0.87; VM covariance defect 15–29% | Sample-dependent maxima, not bounds (0.304–1.135 on independent samples). About 14–29% | `vR17-12:11,13` |
| **Literal N vs N_red** | R18-6 worker: JOINT-CONSISTENT; J1 "a wording fix" ("N must say 'gravitating stress'"; `TESTS:6835`; `rR18-6:49-50,175`) | Literal N with (d-i) is JOINT-CONFLICT whenever W ≠ 0 on a connected expanding slice. N_red is a new completion (P135) | `TESTS:6969-6976`; `vR18-6:5,11`; `refR18-6:26` |
| R18-6 J2 and set A | J2(ii) "proved consistent" (`rR18-6:176`); isotropy from cubic covariance; set A "(d-i) cannot be posed"; 6ℓ²/r² as a Bianchi defect | Quantum J2 OPEN: isotropy needs cubic invariance; the virial step covers free gauge-fixed TT modes only. "Cannot be instantiated as registered". 6ℓ²/r² is a filter correction, not a computed Bianchi defect | `vR18-6:7,9`; `refR18-6:30,34,38` |
| **R16-14:152 non-closure** | "Bianchi holds at O(G²) because F commutes with ∂ and ∂·τ = 0 (comparator)" (`rR16-14:152`) | Wrong: all three filter placements are generically non-conserving, and Π is required. The R16-14 referee had already qualified the claim (`C5_R16-14_referee.md:16`). R18-7's own defect formula and its 1.1–1.4(ℓ/R)² coefficient belong to a hybrid source, not to R16-14's literal placement | `vR18-7:5-9`; `rR18-7:62,82` |
| N̄ in owner Q2 | "Alternative N̄ (mean-field stress) is in tension with `AX:82-83`" (`S23:531,647`) | Not a linear quantum channel, hence not CP in the standard sense (this alone does not imply trajectory-wise loss of positivity). It leaves the CP menu | `vR18-7:11`; `rR18-7:259` |
| R18-7 statements | "K localized in the body"; "exterior vacuum up to erfc tails"; the secular gauge ratios 7e28–2.8e35 as field ratios; "premise (iii) quantitatively no" | Π is causal but not spatially local (algebraic tails). The ratios are energy/variance ratios; amplitudes differ by 2.73e14–5.26e17. The a = 4 cancellation covers only static homogeneous scalar ρ-noise [ref]. [worker, R18-11] It also fails for time-dependent or T_⊥ noise, across gauges, and from E1's zero start; at a = 2, \|ρ_act\| ≥ u₁ | `vR18-7:3,20,22`; `rR18-11:245-252` |
| **R17-11 corrections** | "Unique" exchange current; "(d-ii) still needs W = 0"; receiver from site creation; tadpole "paid with 0 numbers" (`S23:73-75,306-316`) | Unique only among pointwise stresses under H-imp. The universal (d-ii) no-go fails (F3 not confirmed). The free trace is a model postulate, not derived from site creation. "Invisible" means exactly compensated. The bill drops one numerical counterterm, replaced by the stipulated P-vac′ bridge | `vR17-11:20,22-23,28-29,36,39` |
| R17-10 label | Worker: "CERTIFIED-CONFLICT on the fast-only slice 𝓕"; "the sharp-turn limit" (`TESTS:6384`; `S23:183-188`) | A referee-confirmed exact conflict theorem on the conditioned fast face; the uppercase label is not earned even qualified. "Sharp-turn limit" fits realizable zigzag skeletons only. The μ_E remark excludes only constant-multiplier pointwise certificates | `vR17-10:31,33,49` |
| R17-9 root and VU | VM root at stored coordinates; VU "local"; "no SM-count zero under VU" | The stored VM point missed zero (μ_E = −4.75e-5) and needed retuning (μ_T2 = 0.106187). VU is quasi-local, absolutely summable, not finite-range. "No VU zero found" is supported; SM-CONFLICT is not (sign changes near b_γ = 0.1) | `vR17-9:3,7,11` |
| R17-13 Lemma S and μ_E | "C₄ < 0" for the mirror class; μ_E shortfall 2.5–6× | Needs the overlap hypothesis Ŵ′ss′ ≢ 0. The shortfall is search evidence, not enclosed | `vR17-13:7,15` |
| **R18-1 SCREENED** | Worker: SCREENED for (a)–(c); "ξ finite and L-independent at every βU"; Gaussian control passes; S_γ/q² = 0.17–0.21 at βU = 2 (`TESTS:6664-6677`) | OPEN: βU = 4 not reproducibly equilibrated (two ladders gave ξ² = (14.4, 23.0) and (12.5, 10.9)). The supplied control was wrong as written; a corrected one passes. S_γ/q² rises 0.165 → 0.311 over L = 6–16. The L = 2 S(k) comparison was not implemented | `vR18-1:5,7,9` |
| R18-1 Z₀ wording | "The jump equals the static T₂ weight below the gap" | Bracketed by nested cutoff weights. Valid in the uniformly LR-local class; not the broader quasi-local H1 class | `vR18-1:11` |
| **R18-2 NEEDS-STABILIZER** | Worker: met on primary inputs at 2.28σ; "bounded EFT no-go" for the lattice; singlet window m_S ≤ 1.8e11 GeV (`TESTS:6614-6624`) | OPEN: plausible ambiguity treatments give 1.48–3.09σ. The lattice exclusion is scoped to the two dispersions computed (H-EFT, O(1) coefficients). The window bound was a floating-point bug; m_S < 3.17e10 GeV. (S) alone does not require the state to be exactly lowest | `vR18-2:7,9,11,15` |
| R18-4 statements | WX via "regular level cycles"; RB-X for any positive homogeneous extremum; even multiplicity for every factor | Levelset-tame horizontal homology; degree-one conical and degree-two analytic extrema; even multiplicity only for factors with real curve branches (x² + y² counterexample) | `vR18-4:7,9,11` |
| R18-5 statements | "V0 and UD agree only inside the box"; the SM root as an exact zero | False pointwise (mirror directions can cancel); the correct claim is O(1) defects on open off-box regions. A nearby transversal numerical zero, not literal equality at the rounded point | `vR18-5:3,14` |
| R16-8 Lemma F "Consequence" | "The completion cancels the matter's Poincaré defect by a term supported at infinity" (`C5_R16-8_report.md:199-206`) | The defect survives in the complete improved generators: {K_b, P_c} = δ_bc H + Q_D,cb at degree 2. The worker's mechanism (Lemma S∞) has a sign error: in the complete generator, bulk and surface cross-terms cancel, and +Q_D comes from the matter bracket | `vR18-8:7,9-13`; `TESTS:6945` |
| R17-2 Jacobi lemma | Degree-3 failure confined to ker L or the q·v = 0 shell, assuming exact degree-2 closure (`C5_R17-2_report.md:116-126`) | Degree-2 closure fails for the global charges (Theorem A, refereed). The degree-3 form F(Q_D) is formally right but conditional on the singular dressing's boundary domain | `vR18-8:7,17`; `rR18-8:145` |
| R18-8 statements | Corollaries N/N′ "no repair"; the far-field "mass"; thermal invisibility; P-W7edge0 as a physical-state rule; the 2048-site identity | N covers only linear gauge-invariant metric functionals keeping the dipole response; N′ only continuous periodic one-body moments. √(E² − P²) is a frame-dependent translation-charge functional, not an invariant mass. Thermal suppression is conditional on a = ℓ_P, a thermal population and a chosen sensitivity. P-W7edge0 is an initial-state/domain condition. The 2048-site check is a packet test | `vR18-8:7,15,19,23` |
| R18-1's pinch diagnostic [ref, R18-10] | ρ = S_xz(k∥z)/S_xz(k∥y) along the axes, as the pinch test (`TESTS:6666`) | Planar (subsystem) conservation laws in a prepared sector give exact axis zeros while the face and body channels stay screened. Pinch claims must report off-axis channels. R18-1's reading is unchanged: it used the unfiltered ensemble and showed no axis zeros | `vR18-10:11`; `rR18-10:33` |
| R18-10 statements | "Exact canonical sampling" of the fixed-dipole sector; M2 "ergodic"; "a pinch needs S_γ = o(k²)" | The sampler has the exact target measure, but finite MC output is not an exact sample without mixing control. M2 is proved ergodic only at L = 2; at L ≥ 6 agreement is evidence of equilibration. The o(k²) criterion holds for the registered test only, not for the total charge structure factor (R17-6: the vector gap forces only the transverse charge components) | `vR18-10:5,9,13` |
| **Archive import fixes** | Committed runners importing from non-archived paths | R17-7's `r177_enthalpy_orders.py` now imports from `scripts/C5/R11-3`, rerun matches (02:17Z, reported by R18-2). R17-8's runner now points at `scripts/C5/R16-5`, rerun byte-identical (02:47Z, reported by R18-4). An audit of every archived runner's `sys.path` inserts found no other missing directory. (R17-5's fix was dated in S23.) | `TESTS:6625,6745`; `TESTS:6264` |
| SUMMARY §26 labels (carried from S20/S23) | R15-4, R15-6 listed as worker results | **Now fixed in the text** ("Label corrected 2026-10-13"). Closed | `SUMMARY:711` |
| S23 readings superseded | "(S) + (d-i) is a two-sentence package" (`S23:325`); VM as "your choice of law datum" (`S23:694`); R17-9's SM zero "uses the local U vertex, so its only locality question is the vector placement" (`S23:218`) | Three clauses (N_red is needed for β, and literal N conflicts). VM is excluded by covariance. The Dirac vertex V0 was also non-conserved | `vR18-6:11`; `vR17-12:13`; `vR18-5:3` |

Carried, still in force: S23 §5, S20 §5 and S17 §1.8.

---

## 6. Calibration [S26 reading]

### 6.1 S23's round-18 expectations (`S23:868,907,948-953,976`)

| Item | S23 expectation | Refereed outcome | Calibration |
|---|---|---|---|
| R18-1 | SCREENED; (d) OPEN; likeliest failure "MC ergodicity in the βU = ∞ sector" | (a)–(c) OPEN (βU = 4 not equilibrated; βU = ∞ frozen); (d) GAP-CLOSED in the strengthened class | **Physics lean plausible, both readings wrong.** The named failure (βU = ∞) happened, but equilibration at βU = 4 decided the fork. (d) was underestimated |
| R18-2 | NEEDS-STABILIZER; likeliest failure "RECALLED inputs make (b) inconclusive at 2σ, which gives OPEN" | OPEN, for exactly that reason | **Reading wrong; the named failure mode was right** |
| R18-3 | (a) lean V0-NONLOCAL; (b)–(d) OPEN or VU-CERTIFIED-CONFLICT | Dropped: VU excluded by W1 (R17-12). R18-5 found V0 covariant (Lemma M′) but non-conserved (Lemma F) | **Moot as registered. Lean half right:** V0 fails, but on conservation, not locality |
| R18-4 | EXCLUDED-CROSS | EXCLUDED-CROSS | **Right** |

**Score.** One right (R18-4), one right only in its named failure mode (R18-2), one wrong in both readings (R18-1), one moot. S23's round-17 score was three in five (`S23:765`).

### 6.2 Supervisor-registered items, for the wrap-up record

| Item | Expected | Outcome |
|---|---|---|
| R17-9 | OPEN; vector sign "boson-like" (`TESTS:6128`) | OPEN [ref]; SM-LIFTED only with VM admitted; the sign is Dirac-like. **Reading right, sign premise wrong** (as S23 noted) |
| R17-10 | CERTIFIED-CONFLICT for K₆ if margins beat the relaxation gap; μ_E OPEN (`TESTS:6226-6228`) | K₆ OPEN, μ_E OPEN [ref]. **K₆ wrong; μ_E right** |
| R17-11 | SIGNALS (`TESTS:6250`) | CONSISTENT [ref, with corrections]. **Wrong** |
| R17-12 | FREE at O(q) (`TESTS:6363`) | Both FORCED via exclusion; NEITHER; O(q²) free *within* VW [ref]. **Wrong fork; right that the placement is O(q²) law data** |
| R17-13 | SIGN-DEFINITE on D1, a separate knob (`TESTS:6383`) | ZEROED; both signs [ref]. **Wrong** |
| R18-5 | V0-FAILS, "the Wilson mass must couple"; SM OPEN (`TESTS:6653`) | V0-FAILS with exactly that mechanism [ref]; SM-LIFTED-CONSERVED conditional on signed stencils. **V0 right; SM reading wrong unless signed stencils are refused** |
| R18-6 | JOINT-CONSISTENT in C-box; (d-i) not posable in set A (`TESTS:6711`) | Literal JOINT-CONFLICT; N_red consistent; set A OPEN [ref]. **Substance right, literal reading wrong.** The expectation's "N's gravitational-energy source is Λ-free once e₀ is subtracted" silently used N_red |
| R18-7 | CONSTRUCTED with LL gauge dependence the main caveat; premise (iii) forced (`TESTS:6736`) | CONSTRUCTED in scope [ref]; the gauge caveat is real (the Poisson-gauge kernel is not preserved); premise (iii) not forced (a-dependent, static scalar channel only). **Reading right; premise (iii) wrong in R18-7's scope** (and R18-11 [worker] finds it forced at a = 2) |
| R18-8 | ANOMALY ∝ Q_D in {K, P}; invisible thermally below ~1e19 GeV (`TESTS:6778`) | ANOMALY [ref], already at degree 2; thermally tiny below ~1e18 GeV under stated assumptions. **Right** (one decade off on the threshold) |
| R18-10 | PINCH-PRESENT; "dipole conservation makes the charges hyperuniform" (`TESTS:6897`) | OPEN [ref]: no pinch; the fixed-dipole sector is screened with R18-1's ξ; the registered moves fragment. **Wrong, on the mechanism**: dipole conservation on moves fixes only six totals |
| R18-11 | OPEN; the main risk "no natural a works, which would revive R15-2's overshoot" (`TESTS:6942`) | [worker] OPEN with a NOISE-OVERSHOOT candidate at the unique gauge-independent a = 2. **Reading right; the named risk is what happened** (referee running) |
| R18-9 | FOUR-ROW-ZERO with 4 knobs; "UD's smaller Dirac μ_E pull plus the signed stencil should relax the budget" (`TESTS:6869`) | [worker] FOUR-ROW-ZERO on the letter with 4 tunings + a photon window. The mechanism was wrong: μ_E is vertex-independent; the stencil decouples the photon's Ξ from its μ_E. **Reading right, mechanism wrong** (referee running) |
| R18-12, R18-13 | SELF-CLEANING; OFF-AXIS-COUNTED with two extra conditions | [pending] |

**Pattern.**
- **S23's lesson held.** "When the governing no-go's hypotheses include a presentation, a bridge or a vertex datum, expect OPEN plus a new owner question" (`S23:790`). Round 18 bore it out: R18-1 OPEN, R18-2 OPEN, R18-5 conditional on a new owner question (signed stencils), R18-6 a new completion (N_red), R17-12 new law data.
- **The clean results were structural.** R18-4 (topology of analytic bands), Z₀ (Lieb–Robinson plus Schur) and R18-8's Theorem A (degree counting in the improved generators) have no presentation or bridge in their hypotheses. R18-8's observable does, and that is where its corrections fell.
- **New pattern: letter vs substance.** Four verdicts turned on the wording of a fixed reading, not on the physics:
  - R17-12: both FORCED clauses met by exclusion;
  - R17-13: ZEROED on the letter;
  - R18-5: "stencil" did not exclude signed weights;
  - R18-6: literal "total stress".
- **Lesson for round 19.** Each fork should have an explicit "neither" branch. Each registration should say whether law data may be signed or new. Each tested piece is tested as written; any restatement is reported as a new completion and priced. §7's rules add these.

---

## 7. Draft round-19 pre-registrations (readings fixed before any run)

**Rules (as rounds 2–18, `TESTS:5688-5706`, `TESTS:6395-6406`).**
- Probes on Opus 5.5 at xhigh. Every FAIL, EXCLUDED, OBSTRUCTED, CONFLICT or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded.
- Prices are named, never adopted. Prior art is grepped first and counted once. Hypotheses come before titles. Numbers from memory are labelled RECALLED.
- Every law states its whole-zone v_max, gauge fields included. Every count states its counterterm basis. Every Λ mechanism says what is enforced and what is stipulated.
- Round-18 rules kept: locality of vertices (Lemma M, with Lemma M′ for spinors); number-free ≠ forced; bounded classes for spectra; certificates stated in advance.
- **New (from round-18 verdicts):**
  - **Exhaustive forks.** Every fork of the form FORCED-X / FORCED-Y has an explicit NEITHER branch (`vR17-12:17`).
  - **Literal first.** A registered piece is tested as written. A restatement is reported as a new completion and priced (`vR18-6:5`).
  - **Signs of law data.** Each registration says whether law-data weights may be signed (`vR18-5:16-20`).
  - **Equilibration stated in advance.** Any MC reading states its equilibration criterion (round trips, seed stability, ladder) before the run (`vR18-1:9`).
  - **Same-component controls.** A control measures the same component and normalization as the observable (`vR18-1:7`).
  - **Off-axis pinch checks.** Any pinch claim reports the face and body channels, not the axes only (R18-10's correction to R18-1's diagnostic, `TESTS:6982`; `vR18-10:11`).
  - **Thresholds recomputed.** A printed window or threshold is recomputed in exact or interval arithmetic before it is quoted (`vR18-2:11`).
  - **Invariance, not covariance.** Isotropy claims cite the invariance of the state (`vR18-6:7`).
  - **Vertex conservation.** Every TT or stress vertex passes the Lemma-F forward test, or is labelled non-conserved (`vR17-12:5`; `vR18-5:3`).

**Timing.** Each item is sized for about 75 minutes of worker time. No new probe starts after 09:57Z; the campaign ends at 10:57Z. At about 03:30Z that leaves room for about five more rounds.

**Overlap check (running items are not duplicated).**
- R18-9 (worker FOUR-ROW-ZERO) covered the four axial rows at SM counts. **R18-13 (running) covers the off-axis rows at the SM root. No round-19 item drafts either; S26's earlier R19-4 is withdrawn.**
- R18-10 (refereed OPEN) covered static dipole-conserving ensembles. R19-1 covers dynamics (the dispersion of the tensor branch), on R18-1's ensemble.
- R18-11 (worker OPEN; referee running) covers set A on a Minkowski background in Poisson gauge. R19-2 covers only the FRW step its report names as decisive (`rR18-11:271`).
- R18-8 (refereed ANOMALY) covers W7's algebra, and **R18-12 (running) covers the relic population, its bounds and whether P-W7edge0 holds dynamically. No round-19 item drafts either.** (An earlier S26 draft of a W7 relic item was withdrawn when R18-12 was registered.)
- R18-6 covers the classical bridge. R19-3 covers only the quantum J2 step that `vR18-6:7` leaves open.

**Priority.**
1. R19-1 (graviton dynamics) and R19-3 (J2), in parallel, now.
2. R19-2 (set A in FRW), after R18-11's referee confirms Theorem G and Lemma P, or now with its readings conditional on them.
3. (R19-4 withdrawn: R18-13 covers it.)

---

**R19-1. Graviton production from the Z₂ window: can a tensor branch be light-like at or near the RK point?**

- **Plain question.**
  - Z₀ (refereed, bounded) says a statically visible gapless tensor branch with a strict vector gap forces a pinch point. R18-1 (refereed OPEN) and R18-10 (refereed OPEN) found no such static window yet.
  - A static pinch point is necessary, not sufficient. Production needs a light-like branch, ω = ck.
  - At a Rokhsar–Kivelson (RK) point the quantum dynamics is similar to the classical Markov generator of the same ensemble. The single-mode (Bijl–Feynman) bound gives ω(k) ≤ f(k)/S(k), where f is the f-sum (R17-1: k⁰ or k² for the Z₂ models) and S the static structure factor.
  - With S finite at a pinch point, f ∝ k² gives z = 2 and f ∝ k⁰ gives a gap. A light-like branch needs S_TT ∝ |k|, a quantum (non-RK) Coulomb-type phase.
  - Question: in the RK family on N0914's slots, can any tensor branch be light-like? If not, what exactly must the non-RK deformation supply?
- **Setting.**
  - N0914's slots, mod-2 law, the shift action (P112), the E⊕T₂ readout of R18-1.
  - RK Hamiltonians H = Σ_moves [−t·flip + v·(potential)], at t = v, for R18-1's ensemble. (R18-10's fixed-dipole sector has the same ξ [ref, `vR18-10:7`], so it adds nothing.)
  - Observables: the RK-point f-sum f_TT(k) as an exact classical average; S_TT(k) from MC (R18-1's data and runners, rerun first); the SMA bound along axis, face and body directions; the spectral gap of the Markov generator restricted to the TT channel, on small L by exact diagonalization where feasible.
  - Excluded: integer-law lifts; non-local moves; degenerate grounds; the t ≠ v quantum phase beyond leading order.
- **Prior art (count once):**
  - R18-1 and vR18-1 (Z₀; the ensemble; frozen βU = ∞); R18-10 and vR18-10 (OPEN: the dipole is six label totals; planar laws fake axis pinches); R17-6 and vR17-6 (Theorems G, Z); R17-1 and vR17-1 (f-sum orders, k⁰/k² models); R15-5 (worker: qubits give k³ at every finite order at strong coupling);
  - RK-point dynamics of classical Coulomb phases has z = 2 (Henley; Moessner–Sondhi; comparators, RECALLED);
  - quantum Coulomb phase away from the RK point has ω ∝ k (Hermele–Fisher–Balents; comparator, RECALLED);
  - rank-2 and lattice-graviton qubit models (Xu; Gu–Wen; Pretko; comparators, RECALLED).
- **Removed hypothesis.** Statics only.
- **Probes.**
  - (a) The RK-point f_TT(k): its leading k-order in the registered ensemble, as an exact classical expression.
  - (b) The SMA bound ω_SMA(k) = f/S along axis, face and body directions (R18-10's diagnostic correction), at βU ≤ 3.5, where vR18-1 accepts the data.
  - (c) Analytic. For local RK generators with the mod-2 law, prove z ≥ 2 (or a gap) for every T₂ branch, or exhibit a counterexample. State the needed hypotheses (detailed balance, locality, the conserved structure).
  - (d) What a light-like branch needs (S_TT ∝ |k|), and the leading t ≠ v correction to S_TT, if it fits in time.
  - (e) Prices.
- **FIXED readings.**
  - **RK-Z2:** a refereed proof that, in the stated RK class, every T₂ branch is gapped or has z ≥ 2. Light-like production then needs a non-RK phase.
  - **LIGHT-LIKE-SMA:** an explicit ensemble in the stated class whose SMA bound is linear in k in the TT channel, with checked strict V/S gaps. Checked.
  - **NEITHER:** both fail; for example, the bound is z = 2 on samples but no proof covers the class.
  - **OPEN:** otherwise.
- **Expectation.** RK-Z2.
  - Removed hypothesis: statics. RK dynamics is a symmetric Markov generator, and conserved local structure gives diffusive (z = 2) relaxation (comparator).
  - The likeliest failure is a k⁰ f-sum (R17-1's face-only model) making the SMA bound uninformative (a gap). That gives NEITHER or OPEN.
  - If RK-Z2 holds, the graviton window becomes "a non-RK quantum phase with S_TT ∝ |k|", which is P96 stated as a measurable target for quantum MC.

---

**R19-2. Set A's record noise in an expanding universe: does the a = 2 noise settle into a positive cosmological constant, and can it be the observed dark energy?** *(Launch after R18-11's referee confirms Theorem G and Lemma P, or now with the readings conditional on them. If the referee rejects either, the item is moot. This replaces an earlier S26 draft on W7 relics, which R18-12 now covers.)*

- **Plain question.**
  - R18-7 (refereed, in scope) builds set A's E1 + N_c at O(G²) in harmonic gauge.
  - R18-11 (worker; referee running) finds that only the insertion a = 2, the record as √−g T^{μν}, makes the averaged noise source independent of the readout gauge (Theorem G). On Minkowski, Lemma P pins the noise's mean energy at its zero start, so only its pressure acts. At a = 2 the active density is negative and |ρ_act| > ρ_Λ over all of R15-2's window (×1.17 to ×1e19): a NOISE-OVERSHOOT candidate.
  - R18-11 also suggests, without building it, that in FRW the switched-on noise settles to w = −1 with ρ ≈ (1 + ⟨x²⟩ + 2r + u_V/u₁)u₁/3 > 0. That equals ρ_Λ at ℓ ≈ 3.65 µm at the τ_c ceiling (`rR18-11:211-216`). Its report names this as one of the deciding computations (`rR18-11:271`).
  - Question: with an FRW version of Π, does the a = 2 noise become an exact w = −1 component? If so, is its size a prediction (one relation between ℓ and τ) inside R15-2's window and R6-4's lab bounds, or does it overshoot everywhere?
- **Setting.**
  - E1 + N_c at a = 2 (P145); R15-2's channels (ρ, T_⊥, V, TT) at the least-decoherence split; P76; P88 (extended to TT only, as R18-11 states for Poisson gauge).
  - A spatially flat FRW background with matter and radiation; the O(G·noise²) mean source; a noise spectrum stationary in comoving units.
  - An FRW version of Π: a causal conserving completion with zero homogeneous data before t₀. Any homogeneous-pressure freedom is stated as a price, not used to cancel.
  - Both energy histories, (P) and (U) (P146).
  - Excluded: E2; strong field; a ≠ 2; the γ-trade (P-r15c) except as a stated price.
- **Prior art (count once):** R18-11 (worker; its referee when back); R18-7 and vR18-7 (Π, the CP instrument, the scoped a = 4 zero); R18-6 and vR18-6 (set A: (S) cannot remove a non-vacuum stress); R15-2 and vR15-2 (u₁, the window, premise (iii)); R14-2 (the τ_c ceiling, suggested); R6-4 (the window's endpoint); R16-14 and vR16-14 (the Mercury bound); averaged backreaction (Isaacson; Green–Wald; comparators, RECALLED).
- **Removed hypothesis.** The Minkowski background of R18-11's Lemma P.
- **Probes.**
  - (a) The FRW Π and the homogeneous mode: prove or refute ρ̇_K + 3Hρ_K = −3H(ρ_s + p_s) and the w → −1 attractor; state the decaying remainder.
  - (b) The late-time ρ_noise in all channels (r, u_V, ⟨x²⟩ from R15-2's spectrum), as a function of (ℓ, τ).
  - (c) Where ρ_noise = ρ_Λ, and whether that point lies inside R15-2's window and R6-4's bounds; the local Mercury bound at that point (R18-11's a = 2 exclusion of ℓ ≲ 2.5e-8 m).
  - (d) Prediction or tuning: state the precision any match requires.
  - (e) Prices.
- **FIXED readings.**
  - **NOISE-IS-Λ:** an explicit FRW construction in which the a = 2 noise tends to w = −1 with ρ_noise = ρ_Λ at a stated (ℓ, τ) inside the window, consistent with Mercury and R6-4's bounds, with the required precision stated. Checked.
  - **NOISE-OVERSHOOT-FRW:** a refereed demonstration that in the stated class the late-time |ρ_act| exceeds ρ_Λ at every (ℓ, τ) in the window.
  - **NEITHER:** the attractor exists, but its size cannot match ρ_Λ anywhere in the window without the γ-trade or a tuning (state which).
  - **OPEN:** otherwise.
- **Expectation.** NEITHER, leaning NOISE-IS-Λ only at the window's top corner.
  - R18-11's suggested match needs the τ_c ceiling (itself suggested, R14-2) and small r and u_V. The T_⊥ and V channels add positive terms (2r, u_V/u₁) that push the match toward or past the window's edge.
  - Removed hypothesis: the Minkowski background. Kept: a = 2; E1's zero-energy start.
  - If NOISE-IS-Λ holds, set A would produce dark energy from its own record noise, with (S) setting the vacuum part to zero. That would be the campaign's first number that comes out rather than being tuned. It would also make P-r15c unnecessary at that point.

---

**R19-3. (S) as a quantum statement (J2): is the graviton's own zero-point stress absorbed by (S) and (d-i) in every gauge?**

- **Plain question.**
  - vR18-6 confirms the classical bridge (S) + (d-i) + N_red. It leaves the quantum step J2 OPEN (`vR18-6:7`):
    - isotropy needs the vacuum to be cubic-*invariant*;
    - the virial identification of ⟨t_LL⟩₀'s energy with the Hamiltonian zero-point covers only free, gauge-fixed TT modes;
    - constraints, ghosts, interactions and the gauge-dependent LL pseudotensor are not covered.
  - For linearized gravity on the box regulator, is the one-loop gravitational vacuum stress of the absorbable form −e_g g + W_g h[n] in every gauge, with e_g the TT zero-point energy density? If yes, (S) with the gravity sector inside H, plus (d-i), removes it with no number. If a non-absorbable part depends on the gauge or on the pseudotensor, J2 needs a named observable bridge.
- **Setting.**
  - R9-9's N-type box graviton (whole-zone v_max stated), lattice frame, Fierz–Pauli quadratic action.
  - Three treatments: reduced phase space (TT only); harmonic gauge with Faddeev–Popov ghosts; Coulomb/Poisson gauge.
  - The one-point stress via (A) ⟨t_LL⟩, (B) the second-order Einstein tensor ⟨G^(2)⟩ (Isaacson-type), and (C) the Hamiltonian zero-point. One loop.
  - Check cubic invariance of each vacuum, not just covariance.
  - Excluded: graviton self-interaction beyond one loop; matter; backreaction.
- **Prior art (count once):** R18-6 and vR18-6/refR18-6 (J2); R17-11 and vR17-11 (the exchange current); R17-7 (the enthalpy residual); R11-3 (zero-point stress of lattice fields); R9-9 (graviton symbol); the Isaacson effective stress and the gauge independence of the on-shell one-loop effective action (comparators, RECALLED).
- **Removed hypothesis.** Free TT-only, gauge-fixed modes.
- **Probes.**
  - (a) ⟨G^(2)_μν⟩ and ⟨t_LL⟩ in each of the three treatments, on the box regulator.
  - (b) Decompose each into −e g + W h[n] plus a remainder; check cubic invariance; compare e with the TT zero-point.
  - (c) Does the remainder vanish, and is it gauge-independent?
  - (d) Under (S) with the gravity sector inside H, plus (d-i): is the gravitational vacuum removed with no number?
  - (e) Prices.
- **FIXED readings.**
  - **J2-ABSORBED:** in all three treatments, the one-loop gravitational vacuum stress has the form −e_g g + W_g h[n], with e_g equal to the TT zero-point energy density and no remainder. Checked.
  - **J2-GAUGE-BRIDGE:** a refereed demonstration that the non-absorbable part depends on the gauge or the pseudotensor choice, so J2 needs a named observable bridge.
  - **NEITHER:** a gauge-independent non-absorbable remainder (J2 fails outright in the stated class). Refereed.
  - **OPEN:** otherwise.
- **Expectation.** J2-ABSORBED for (B) and (C); (A) may differ.
  - On shell, the one-loop effective action is gauge-independent (comparator), and ghosts cancel the unphysical polarizations, leaving the two TT modes.
  - In the lattice frame the vacuum is cubic-invariant, so its one-point stress is isotropic.
  - The likeliest failure is ⟨t_LL⟩'s off-shell gauge dependence, which would make (A) disagree and give J2-GAUGE-BRIDGE for the pseudotensor reading only.
  - Removed hypothesis: free TT-only modes. Kept: one loop, box regulator.

---

**R19-4 (withdrawn at 03:42Z).** Its question, the off-axis rows for UD and VW at the SM root, is now R18-13 (pre-registered 03:40Z, running; `TESTS:7061-7091`). R18-9 [worker] already found face2 ≠ T₂g for UD (`TESTS:7055`). So round 19 has three items.

**Queued for round 20 (stubs only; register after the named reading).**
- W7: if R18-12 returns BOUNDED or OPEN, the observational test of √(E² − P²) under the ADM readout bridge that P141 names.
- The bill's off-axis fallback (P122 as a non-shape knob, or a q²-dependent seagull), if R18-13 returns OPEN or its count exceeds the placement data.
- Quantum MC of the t ≠ v Z₂ model for S_TT ∝ |k|, if R19-1 returns RK-Z2.
- W15's continuous multi-shift mixing (`vR18-4:3`), if time allows.

---

## 8. Draft of the 10:20Z wrap-up (as complete as possible at about 03:55Z)

Items marked **[UPDATE AT CLOSE]** depend on readings not yet in. Each gives the text to use for either outcome.

### 8.1 Plain-words section for SUMMARY (proposed §27; replaces S23 §8.1)

> ## 27. Campaign C5, rounds 16–18: one classical source rule, a qubit window that needs a pinch point, and a cone bill on conserved vertices (2026-10-12/13)
>
> **What these rounds did.** Rounds 16–18 asked whether the remaining walls could be closed by proof or by counting. There were 39 probes: 14 in round 16, 13 in round 17 and 12 in round 18 (one round-18 item was dropped before launch when its premise was excluded). By 03:48Z, 35 had verdicts from a codex gpt-5.6-sol referee. **[UPDATE AT CLOSE: the count of verdicts, and any round-19 items.]** The probes and every synthesis are Claude Opus 5.5, the same model family. Nothing was adopted.
>
> **What gravity feels (Λ and β).**
> - The four axiom texts force no rule that removes the cosmological constant. Making gravity ignore a fixed number is a tuning (R16-6, R17-3, refereed).
> - One rule needs no number: "the law's lowest state weighs nothing", (S). It is consistent and not a disguised tuning, but it would have to be **added** (R17-3, refereed).
> - The grid vacuum also has a pressure that (S) cannot cancel. Handing that pressure to the sector that creates new sites as space expands is consistent and sends no faster-than-light signal, with no number (R17-11, refereed). The receiver is a model assumption, not derived from the axioms.
> - Mercury needs gravity's own energy to gravitate (R16-14, refereed). Stated literally ("the metric is sourced by all stress, vacuum included"), that rule contradicts the pressure hand-off. Restated as "the metric is sourced by matter plus the vacuum's energy above the lowest state, plus gravity's own stress", the three rules together give exactly Einstein's equations: Mercury right, zero leftover Λ if our vacuum is the lowest state, no faster-than-light channel. That is three added sentences and no number. The restatement is a new rule, not a rewording (R18-6, refereed).
> - Whether the same works when gravity itself is quantum is open (R18-6).
> - **A test in particle physics.** Under (S), our Higgs vacuum must be the true minimum. With only Standard-Model particles that requires a top-quark mass of at most 170.9 GeV. The recalled measurements lie 1.5–3.1σ above it: suggestive, not decisive. Otherwise new particles must exist below about 1e11 GeV: a singlet scalar (one tuned mass) or two or more vector-like 5-plets (no tuning). The grid itself cannot stabilize the vacuum (R18-2, refereed OPEN).
> - **Set A** (a smooth continuum with discrete records): the Mercury fix can be built at second order, as a causal, conserved records-to-metric law. It needs three more stipulated choices: a conserving completion of the source, a gauge, and where the record noise enters. The mean-field version is not a legitimate quantum operation (R18-7, refereed, in a weak-field static scope). Only one way of entering the noise is independent of the gauge, and there the noise's weight exceeds the observed dark energy across the allowed range, unless some noise channels go unrecorded (R18-11, worker). **[UPDATE AT CLOSE: vR18-11; R19-2 (the noise in an expanding universe), if run.]**
>
> **The graviton.**
> - Reading each qubit as a two-state clock escapes the earlier proof that finite slots cannot give Einstein's stiffness (R17-1, refereed). The explicit models found are not gravitons.
> - In a broad class of local qubit models, a graviton with gapped vector and scalar partners that the readout can see must show a "pinch point" in its static response, whatever its stiffness (R17-6, R18-1, refereed in bounded classes).
> - In the simplest local ensemble that penalizes the leftover charges, no pinch point was seen. Weaker penalties look screened; the strongest is not settled (R18-1, refereed OPEN).
> - Conserving the charges' dipole moment does not help: it fixes only six global totals (R18-10, refereed OPEN). **[UPDATE AT CLOSE: R19-1 (a light-like branch), if run.]**
> - A supplied graviton is still the only known source.
>
> **One light cone for everything.**
> - One of the two graviton–matter vertices used since round 9 (M) is non-local (R17-4, refereed).
> - The campaign's own conservation test then removed both photon placements tried (R17-12) and the Dirac vertex used since round 16 (R18-5, refereed). The earlier "Dirac birefringence" obstruction belonged to that vertex.
> - On the surviving vertices, Standard-Model particle counts zero the graviton-cone and one shear row with three tuned numbers, if one placement weight may be negative (R18-5, refereed conditional). The other shear row can be zeroed by one edge shape on its own (R17-13, refereed). A worker found all four zeroed together, with four tuned numbers and a narrow window for the photon's dispersion (R18-9, worker). The off-axis graviton speeds are not yet paid: for fermions they add at least one condition (R18-9, worker). **[UPDATE AT CLOSE: vR18-9; R18-13.]**
> - The conditional bill is at least 9 tuned numbers plus the cosmological constant (plausibly 9–11 once the photon window and the fermion off-axis rows are counted), each to 1e-13 to 1e-16. It drops by one with the pressure hand-off and by one more with (S). The vertex details beyond the conservation test are law data that nothing fixes.
>
> **Comparing graviton and light speeds on a grid (GW170817).** For free matter with finitely many smooth bands, every way tried of making that comparison gauge-invariant fails, now including band crossings and Weyl points (R16-5, R17-5, R17-8, R18-4, refereed in their classes). What is left: an infinite tower per cell, a discontinuous momentum, a non-canonical shift action, non-smooth or many-band matter, or interactions.
>
> **The off-box tail (W7).** Its bulk part is gravity's own Coulomb-type field in lattice variables (R17-2, refereed OPEN). At infinity, the total energy, momentum and boost charges fail the Poincaré relations by exactly the defect charge of particles at the zone edge, and no completion of the gravity sector can cancel this at leading order (R18-8, refereed). For a body containing such particles, the far-field charges would depend on its speed relative to the grid. Thermal populations make this tiny below about 1e18 GeV; a population left over from the start is not bounded. **[UPDATE AT CLOSE: R18-12 (relic edge quanta).]**
>
> **Status.**
> - Nothing was adopted.
> - New owner questions: the three-sentence source rule; the top-quark bet or new particles; vertex law data and signed weights; the W7 anomaly or a no-edge-quanta condition; set A's noise insertion (a = 2 or a = 4) and the γ-trade.
> - Pending at close: **[UPDATE AT CLOSE: from §8.3.]**

### 8.2 PRICE_NOTE v7 delta (proposed; replaces S23 §8.2's status line and extends its rows): campaign C5's prices, P15–P147 (named; none adopted)

**Status line (replace `PRICE_NOTE:3`).** "DRAFT v7: v6 plus campaign C5's ledger P15–P147 (syntheses S5–S26). Every price is named, none adopted. Prices refereed as FAIL, non-local or non-conserved (P74, P120, P123, P126, P127 as a covariant vertex with R9-9's graviton, and P108's V0 half) are listed so the owner can see them; they are not payable under the registered readings. Rows marked [worker] rest on unrefereed items. P143 is named so the owner can see it; it buys nothing static."

**Rows.** Format: price — axiom text touched — source. "None" means a dynamical or tuning choice the axioms leave downstream (`AX:114-130`).
- **P15–P106:** as S23 §8.2 (`S23:1034-1127`), except these replacement rows:
  - P52 Site creation (rate 3H); also the receiver for (d-i), valid inside H-imp, not derived from the lattice axioms — `AX:37,40`; `AX:182-184` — `S14:183`; `vR17-11:22-23`
  - P70 Vacuum bridge. (d-i): consistent and non-signalling in class 𝒟, number-free, conditional bookkeeping that replaces a trace counterterm. (d-ii): pairing or ≥ 2 tunings per species; the universal (d-ii) no-go is withdrawn — `AX:187`; `AX:47` (pairing) — `S17:224`; `vR17-7:21-30`; `vR17-11:36,39,44-45`
  - P92 (S): the law's lowest state weighs nothing. Number-free; consistent; unforced; conditionally viable; with (d-i) and P135 a three-clause, zero-number classical bridge — `AX:187`; `AX:116-130`; `AX:94` (reading) — `vR17-3:17`; `vR17-7:69-70`; `vR18-6:13`
  - P93 Late-vacuum stability. With SM content only: M_t(pole) ≤ 170.88 GeV (two loops; recalled inputs 1.48–3.09σ above, not robust); otherwise new content below about 1.8e11 GeV (P131, P132). Applies once the observed vacuum source is identified with the energy above the law's ground — `AX:187` — `vR18-2:5-7,15`
  - P96 Emergent constraint not dressing-connected (= P-r17-6d). Signature: a pinch point, necessary in the uniformly LR-local class (Z₀); finite-fugacity screening OPEN — none (dynamical) — `vR17-6:13`; `vR18-1:9,11`
- **P107–P128:** as S23 §8.2 (`S23:1130-1151`), except these replacement rows:
  - P107 Completion N. Literal N conflicts with (d-i) when W ≠ 0 (W18); in C-box-E use P135. In set A, R16-14's unprojected N is non-conserving; the construction N_c = P107 + P138 + P139 + P140 holds in the weak-field harmonic static/quasi-static scope — `AX:82-83`; `AX:187` — `vR16-14:15`; `vR18-6:5`; `vR18-7:5-9,26`
  - P108 SF Dirac strain flow (stipulated). **The V0 vertex half is withdrawn: V0 fails the forward Ward value** — `AX:187` — `vR16-13:5`; `vR18-5:3`
  - P109 Wilson-Dirac μ_T2 row: one continuous Dirac-edge shape tuning per edge (refereed ZEROED), or Clifford-flat 8-component fermions — none / `AX:47` — `vR17-13:13,17`
  - P122 K₆ off-axis condition; exact conflict with the axis zeros on the conditioned fast face (Theorem F), local persistence; OPEN on 𝒮; extended to fermions (UD face2 ≠ T₂g) [worker, R18-9] — none; `AX:187` for a vertex datum — `vR17-4:5`; `vR17-10:53`
  - P126 Stipulated vector TT vertex VU. **Not conserved (fails Lemma F); not payable under W1-s** — `AX:187` — `vR17-12:5-11`
  - P127 VM placement = keeping a one-sided magnetic placement. **Not covariant with R9-9's graviton (Lemma C); payable only with a graviton whose h_xy sits at z + ½** — `AX:187`; `AX:57-58` — `vR17-12:13`
  - P128 Non-Lagrangian partner for (d-i); excluded only for a single ultralocal P(X) — `AX:187` — `vR17-11:35`
- **New rows (rounds 17–18):**
  - P129 VW placement stencils as law data (signed weights allowed) — `AX:187` — `vR17-12:15`; `vR18-5:16`
  - P130 A move set that unfreezes the charge-free Z₂ sector — `AX:57-61` (dynamics) — `vR18-1:5`; `rR18-1:231`
  - P131 Higgs-portal singlet: one unprotected scalar-mass tuning per species; m_S < 3.17e10 GeV — content, no axiom line — `vR18-2:11`
  - P132 Vector-like Dirac 5-plets, n5 ≥ 2, chirally protected: no tuning — content; needs chirally protected lattice fermions — `vR18-2:13`
  - P133 The Dirac pair block as law datum (the family 𝔇, which forces UD) — `AX:187` — `vR18-5:7`
  - P134 The Dirac O(q²) placement [worker] — `AX:187` — `rR18-5:309`; `vR18-5:22`
  - P135 N_red: the metric sourced by T_m − (V − e₀)g plus gravity's own stress. A new completion — `AX:82-83`; `AX:187` — `vR18-6:5,13`
  - P136 J2: the supplied graviton is GR's self-coupled field, and its quantum sector lies inside the H that defines e₀. Quantum step OPEN — `AX:47`; `AX:187` — `vR18-6:7`
  - P137 A conserved meter-sector stress for set A's noise injection [worker, suggested] — `AX:185`; `AX:187` — `rR18-6:177`
  - P138 Causal conserving projection Π (causal, not spatially local) — `AX:187` — `vR18-7:3,26`
  - P139 Harmonic gauge for set A's O(G²) readout; the Poisson-gauge noise kernel is not preserved; immaterial for the mean at a = 2 [worker] — `AX:82-83` — `vR18-7:22-24`; `rR18-11:233`
  - P140 Noise insertion weight a (one number); zero static scalar active density at a = 4 [ref, scoped]; gauge-dependent for time-dependent noise [worker] — `AX:82-83`; `AX:187` — `vR18-7:20`; `rR18-11:245-251`
  - P141 Accept the asymptotic Poincaré anomaly ({K_b, P_c} = δ_bc H + Q_D,cb at leading order) — `AX:57-61`; `AX:82-83`; `AX:187` — `vR18-8:23,25`
  - P142 No edge quanta in the initial state (an initial-state/domain condition) — none — `vR18-8:23`
  - P143 Dipole conservation on the moves (≡ six label totals); buys nothing static in the tested couplings [ref] — `AX:57-61`, `AX:116-123` — `vR18-10:3,7`; `rR18-10:250`
  - P144 Planar diagonal-label laws (3L frozen plane charges; fragmentation) [ref] — `AX:57-61`; `AX:37-41` — `vR18-10:9`; `rR18-10:251`
  - P145 The record as √−g T^{μν} (a = 2), the unique readout-gauge-independent insertion; the γ-trade then becomes necessary [worker] — `AX:82-83`; `AX:187` — `rR18-11:142,233`
  - P146 The S/V noise's energy history ((P) zero start, or (U) a pre-loaded datum) [worker] — `AX:92-95`; `AX:185` — `rR18-11:234`
  - P147 The photon window (b_γ ≈ 2.936–2.947), needed for all four axial rows at SM counts [worker] — `AX:187` — `rR18-9:307-310`

**Count-once notes for the note.**
- P51 = P-Tad = P70's uniform part = R17-7's enthalpy residual (`vR17-11:39`).
- P63(iii), P129, P133, P134: four instances of one unfixed object, the graviton–matter vertex beyond the forward Ward value.
- P137, P140/P145, P146 and premise (iii): one quantity, set A's active noise density, priced separately until R18-11 is refereed [S26 reading].
- P96 = P-r16-7a = P-r16-11a = P-r17-6d. P112 = P-r17-1c = P-r17-6a. P92 = P-r166a = P-r173a. P-r177b = P4. P-r1711a = P52/P53. P-r1711b = P68's existence hypothesis. P-R17-9d = P100. P-R17-12c = P127. P-R17-13a = P109. P-W7bdy = P117 → P141 [worker]. P-pf1 = P90.

**"In plain words" addition (proposed for §1; replaces S23's).** "On a slower-than-light grid, every relativity test computed so far can be met at no fewer than nine tuned numbers plus the cosmological constant (plausibly nine to eleven), on vertices that pass the campaign's conservation test, with vertex details that nothing yet fixes. Classically, three added sentences with no number make gravity's source exactly Einstein's: the lowest state weighs nothing, the vacuum's pressure goes to site creation, and the metric is sourced by matter plus the vacuum's energy above the lowest state. That predicts a stable Higgs vacuum: a top quark no heavier than about 170.9 GeV, or new particles. The graviton cannot yet be made from the axioms' qubits at any named price except supplying it; a qubit graviton would have to show a pinch point."

### 8.3 Pending at close (as of 03:50Z; the wrap-up must update it)

- **Referees back:**
  - vR18-7: CONFIRMED WITH CORRECTIONS, CONSTRUCTED in the weak-field harmonic static/quasi-static scope — **recorded** at `TESTS:7020-7027` (03:37Z).
  - vR18-8: CONFIRMED WITH CORRECTIONS, ANOMALY met (`SP/ref_R18-8/REFEREE_VERDICT.md:1,3,25`). Record W7 as DERIVED (a boundary anomaly), with the Lemma S∞ sign correction, the narrow corollaries and the observable's status.
  - vR18-10: CONFIRMED WITH CORRECTIONS, OPEN (`SP/ref_R18-10/REFEREE_VERDICT.md:1,15`). Record it, with the communicating-class, L = 2 ergodicity and o(k²)-scope corrections.
- **Referees running:** R18-9 (worker FOUR-ROW-ZERO; `TESTS:7044-7059`), R18-11 (worker OPEN + NOISE-OVERSHOOT candidate; `TESTS:7028-7043`). **[UPDATE AT CLOSE]**
- **Workers running:**
  - R18-13 (off-axis rows at the SM root; ALL-ROWS-ZERO / OFF-AXIS-COUNTED / OPEN; pre-registered 03:40Z, `TESTS:7061-7091`);
  - R18-12 (relic edge quanta; SELF-CLEANING / BOUNDED / OPEN; pre-registered 03:37Z, `TESTS:6988-7019`).
- **Round-19 drafts:** R19-1 … R19-3 (§7), none launched at 03:55Z; R19-4 withdrawn (R18-13). R19-2 is now set A in FRW; the earlier W7 relic draft was withdrawn because R18-12 covers it.
- **Recorded since S23:** vR17-9, vR17-10, vR17-11 (`TESTS:6580-6600`, 02:16Z); vR17-12, vR17-13, vR18-2, vR18-4 (`TESTS:6793-6825`, 03:00Z); vR18-1, vR18-5, vR18-6 (`TESTS:6956-6977`, 03:17Z).
- **SUMMARY:** add §27 (from §8.1). The §26 label fix is already applied (`SUMMARY:711`).

### 8.4 Theorem list additions for the wrap-up (rounds 16–18; cite as "item + name")

Rounds 16–17 through R17-8: as S23 §8.4 (`S23:1190-1204`). Added:

| Item | Result | Verdict |
|---|---|---|
| R17-9 | VU representative-invariant, absolutely summable, quasi-local, correct continuum amplitude; VM three-row SM zero (retuned) | `vR17-9:13` |
| R17-10 | Theorem F (conditioned fast face; local persistence) | `vR17-10:53` |
| R17-11 | (d-i) exchange current Q_ν = ∇^μ(W h_μν); generalized Lemma V; linear non-signalling in 𝒟 | `vR17-11:44-45` |
| R17-12 | Lemma F (forward Ward value, necessary O(q)); Corollary F1; Lemma C; Lemma X (within the Maxwell-product tie); Lemma I | `vR17-12:19` |
| R17-13 | Forms P and I (exact under SF); Lemma S (with the overlap hypothesis); the transversal μ_T2 zero | `vR17-13:17` |
| R18-1 | Theorem Z₀ (uniformly LR-local class; nested cutoff weights) | `vR18-1:13` |
| R18-2 | M_t,crit = 170.8776 GeV, λ_min = −0.01129 (two loops); the scoped H-EFT lattice exclusion; singlet and 5-plet stabilizers | `vR18-2:17` |
| R18-4 | Lemma S0; Theorem WX (levelset-tame homology); Lemma RB-X (degree-one conical, degree-two analytic); Lemmas X1/X2 (parity corrected) | `vR18-4:15` |
| R18-5 | Corollary DF (V0 fails Lemma F); Lemma M′ (spinor faces allowed); Lemma D (UD unique in 𝔇); Lemma D₀ | `vR18-5:22` |
| R18-6 | The net-source reduction (exact GR, TOV without W, β = γ = 1, Λ̃ = 0 under P93, no Lemma-S channel); the literal J1 conflict (Q = 0 ⇒ W = 0 on connected expanding slices) | `vR18-6:13`; `refR18-6:44` |
| R18-7 | E1 + N_c through O(G²) (causal Π; CP instrument; β = γ = 1); R16-14's N non-conserving; N̄ not a linear channel; (2a − 8)\|u₁\| for static homogeneous scalar noise | `vR18-7:26`; `TESTS:7020-7027` |
| R18-8 | Theorem A (degree-2 anomaly, completion-independent); Lemma T; Corollaries N, N′ (narrow); Theorem A3 (conditional); the small-velocity √(E² − P²) formula | `vR18-8:25` (in `SP/`; record in `TESTS`) |
| R18-10 | Dipole = six label totals; the communicating-class measure; fragmentation by planar invariants; the axis-diagnostic counterexample | `vR18-10:15` (in `SP/`; record in `TESTS`) |
| R18-11 [worker] | Theorem G (a = 2 unique gauge-independent insertion); Lemma P (homogeneous energy pinned on Minkowski); the a = 2 budget | pending (`TESTS:7028-7043`) |
| R18-9 [worker] | The SM-count four-row root (U + UD + VW, signed stencil); μ_T2 Dirac-only; UD face2 ≠ T₂g | pending (`TESTS:7044-7059`) |

### 8.5 Provenance: findings never refereed (list in the wrap-up)

- **Carried from S23 §8.3:**
  - R16-1's Z-width transfer to D1;
  - R16-4's E2 memory figure;
  - R16-3's U common zeros (P87's local form). No later referee re-solved one;
  - R16-13's SM-count stall numbers (now also on the non-conserved V0);
  - R17-1's N0914 full-J k⁰ phase;
  - R17-6's best candidate;
  - R17-7's DESI proxy beyond arithmetic;
  - R17-2's escape-3 and escape-5 sketches;
  - R17-8's joint-class sketch.
- **New this period:**
  - R17-9's sampled VU obstruction (supported, not enclosed; `vR17-9:11`), now moot (VU non-conserved);
  - R17-10's P-K6′ in its "finite fraction" form;
  - R17-12's "no SM root under VW0" (sampled solves);
  - R17-13's μ_E deficit of 2.5–6× (search evidence, `vR17-13:15`);
  - R18-1's βU = 4 widths and its Debye-screening reading (`vR18-1:9`);
  - R18-2's 5-plet mass ceilings (not precision results, `vR18-2:13`);
  - R18-4's numerical floors 0.76–0.79 (supporting checks, not the proof; `vR18-4:13`);
  - R18-5's P134 "up to about 10% per field", and its m = 0.001 re-solve at N = 96 only (`rR18-5:348`);
  - R18-6's independence of the three clauses (`rR18-6:164-167`), its set-A noise inclusion, and its 6ℓ²/r² Bianchi reading (`vR18-6:9`);
  - R18-7's 1.1–1.4(ℓ/R)² coefficient (attributed to the wrong source), its "localized in the body" and "erfc tails" claims, and its β = 3 aside (not ruled on) (`vR18-7:3,9`);
  - R18-8's F(Q_D) (conditional), its sign narrative for Lemma S∞ (reversed), its broad "no repair" wording, its thermal sizes as unconditional statements, and its P90 closure off the face (not ruled on) (`vR18-8:9-19`);
  - R18-10's βU = 3–3.5 widths and its M2 ergodicity beyond L = 2 (`vR18-10:9`);
  - **all of R18-9 and R18-11** (worker readings; referees running), and **all of R18-12, R18-13** and any round-19 item **[UPDATE AT CLOSE]**.
- **Syntheses.** S5–S26 and every "[S… reading]" in them are same-family and unrefereed: the wall maps' DERIVED/OPEN and cheapest-price columns, the P-numbering and count-once identifications, the owner questions and the pre-registration drafts.
- **Model provenance.** Workers, supervisor and syntheses: Claude Opus 5.5 (one family). Referees: codex gpt-5.6-sol at xhigh (another vendor), per each `codex_run.log` header.

---

## 9. Caveats

- **Same family, unrefereed.** Everything this synthesis adds is unrefereed and from the same model family as the workers:
  - the DERIVED/OPEN and "cheapest price" columns;
  - W18 and W19 as walls;
  - the P129–P147 numbering and the count-once identifications (notably P137, P140/P145, P146 and premise (iii) as possibly one quantity, and the four vertex-law-data instances as one object);
  - every [S26 reading];
  - the owner questions and the round-19 drafts.
- **Referee verdicts used before they are recorded in `TESTS`.**
  - vR18-7 was read from `SP/` at about 03:33Z and recorded at `TESTS:7020-7027` in matching terms. vR18-8 was read from `SP/` and is not yet recorded; if its recorded wording differs, these change: §1.0 item 8, §1.5, W7, P117/P141/P142, Q8, and §8.1's W7 paragraph. vR18-10 (read from `SP/` at about 03:48Z, not yet recorded) affects §1.0 item 5, §1.3, W2, P143/P144, P96, Q3, the §5 diagnostic rows and R19-1's premise.
  - Unruled worker items inside them stay [worker]: the β = 3 aside; the reduction of P117; P90's degree-2 closure off the face.
- **Worker readings used without a referee.** R18-9 and R18-11 (referees running): §1.0 items 2 and 9, §1.1's R18-9 entry, §1.2's R18-11 entry, §1.6's bill rows, W3, W4, W8, W11, P145–P147, the P139/P140/P-r15c status lines, Q2, Q5, and R19-2's premise. If any referee narrows them, those change.
- **Conditional refereed results.**
  - The R18-5 SM root holds only if signed VW stencils are admitted, and only under the O(q) forward-conservation convention (`vR18-5:18-20`). It is a nearby numerical zero resolved to about 1e-5 in the photon grid (`vR18-5:14`).
  - The C-box-E bridge holds on connected slice components that expand somewhere. Wholly static components need separate treatment (`vR18-6:3`).
  - (d-i) is an on-shell, one-point covariant embedding, not a lattice derivation or a completed action (`vR17-11:44-45`).
  - Z₀ holds in the uniformly LR-local class, not the broader quasi-local H1 class (`vR18-1:11`).
- **Bounded, not class-wide.**
  - R17-12, R18-5: R13-5's symmetric universal-energy W1 class, necessary O(q); no exact W1 completion of any vertex.
  - R18-4: two-band real-analytic Bloch Hamiltonians with H-RB.
  - R18-6: class 𝒟 (smooth, hypersurface-orthogonal, trace equation omitted).
  - R18-2: two-loop RG-improved tree level with recalled inputs; the lattice result is H-EFT with O(1) coefficients.

  **No refereed result says the graviton, Λ or the split is impossible in general.**
- **Prescription scope.** Every Ξ and μ statement uses an R9-9-type graviton, now with the conserved vertices U/UD/VW, SF for the shears, an ultralocal seagull, and a supplied zero-point vacuum. They are bare-cone shifts, not dressed poles. W15 still supplies no gauge-invariant replacement.
- **Scale bridge.** Every Planck-unit number uses a = ℓ_P (`AX:189-190`): the 1e123 enthalpy, the 1.7e19 GeV edge floor, the 1e18 GeV thermal threshold, and the 1e-13 to 1e-16 precisions.
- **RECALLED inputs.** The top mass, the pole-mass ambiguity, the published stability bounds, and the R14-2 τ_c ceiling and R6-4 window endpoint used by R19-2 are recalled or suggested values, labelled as their sources label them.
- **Drafts are proposals for the driver.** Readings are fixed here so they cannot be adjusted after a run. The driver may reorder or drop items. R19-4 was withdrawn because R18-13 covers it, and an earlier W7 relic draft because R18-12 covers it. R19-2's readings are conditional on R18-11's Theorem G and Lemma P (worker; referee running). No draft repeats R18-9 … R18-13.
