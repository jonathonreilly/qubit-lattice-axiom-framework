# C5 S14: synthesis after rounds 10–12 (refereed through R12-4; R12-5 referee, R12-6 and R12-7 workers pending)

**Author.** Claude Opus 5.5 (S14), the same model family as every C5 worker, the supervisor, S5, S8 and S11. **This synthesis is not refereed and gives no verdicts.** Every verdict quoted is a codex gpt-5.6-sol (xhigh) referee verdict as recorded in `TESTS.md` or in the cited `C5_*_referee_verdict.md`. Written 2026-10-12, 20:01Z to about 20:13Z. No repository file was edited.

**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md:3952-4551` (round 10 to the end); `agents/C5_S11_synthesis.md`; `SUMMARY.md:534-635` (§§21–24); referee verdicts `C5_R10-1` … `C5_R10-5`, `C5_R11-1` … `C5_R11-5`, `C5_R12-1` … `C5_R12-4` (`_referee_verdict.md`). **Read in part:** price sections of the worker reports `C5_R10-4:289-310`, `C5_R11-1:309-330`, `C5_R11-2:252-262`, `C5_R11-3:238-255`, `C5_R11-5:238-259`, `C5_R12-1:266-273`, `C5_R12-2:276-286`, `C5_R12-3:241-256`, `C5_R12-4:172-188`; `C5_R11-2_report.md:45-51` (open routes O1–O6); `TESTS.md:1523-1547` (C4 lane RE), `:2380` (F2), `:2399-2404` (O3), `:2985-2993` (R5-3), `:3556` (Theorem E); `agents/C4_F2_referee.md:46`; section headers of `C5_S8` and `C5_S5`. **Pending, used only as pending:** `C5_R12-5_report.md:1-60` (worker; referee running); R12-6 and R12-7 have no reports.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS`, `SUMMARY`, `PRICE_NOTE` are in `P/`; bare `C5_*` are in `P/agents/`; `vR10-1` abbreviates `C5_R10-1_referee_verdict.md` (and so on). `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.

**Labels.**
- **[ref]** referee-confirmed, with the referee's scope.
- **[ref, bounded: …]** a refereed FAIL, EXCLUDED or no-go, with its class.
- **[pending]** R12-5 (referee running), R12-6, R12-7 (workers running). Worker claims, not verdicts.
- **[S14 reading]** an interpretation made here; same family; unrefereed.

**Sets** (as S8/S11). A = continuum base, discreteness only in records. B = Euclidean Z⁴. C = the axioms' Z³ with continuous time, tuned. C-box = Z³ × ℝ with a box-exact law. C-box-S = C-box with a boson–fermion edge pairing.

**Record-keeping note.** `SUMMARY.md` stops at §24 (rounds 8–9, `SUMMARY:608-635`). Rounds 10–12 are recorded only in `TESTS`. §1 below could serve as the plain-words source for a §25; this synthesis does not write it.

---

## 1. What changed since S11, in plain words

### 1.0 The short version

S11 left one question hanging: the grid's leftover "boost anomaly" sits at the edge of the box, and loops carry it back into the light cones. Is there an untuned way out? Three rounds later the answer has a shape, though not a final one.

1. **Matter in the box got better again.** Bound, spinning bodies in a *curved* field (d = 3) move as general relativity says: no internal stress at rest, light-bending γ independent of binding, the 3/2 geodetic precession, unit frame dragging (R11-4, PASS WITH SCOPE).
2. **To cancel the edge anomaly, you need both statistics.** This is now proved, in a stated class: no choice of bands for bosons alone, or fermions alone, cancels an anomaly moment over a range of masses (R11-1, DERIVED). Pairing is necessary there. It is still not sufficient: it cancels the photon's shift, not the electron's (R10-1).
3. **Supersymmetry on the lattice does not, by itself, tie the electron's speed to the photon's.** The simplest supersymmetric photon must have a doubler (R10-5, bounded FAIL). A doubler-free photon multiplet exists (BF), but its charged Hamiltonian has a Coulomb-type long-range term and nobody has computed the split in it (R12-3, INCONCLUSIVE). A single nilpotent supercharge leaves the ratio c_γ/c_e free (vR12-3:9).
4. **The graviton still is not produced.** In the regular class of exact qubit constraints, every graviton frequency is O(k³), so it cannot travel at light speed (R11-2, EXCLUDED in that class). Making the constraint algebra nonlinear did not close (R12-1, INCONCLUSIVE).
5. **Λ moved in two places.** On a fixed grid the vacuum's pressure is not minus its energy (w ≥ 0), so a flat vacuum needs two conditions, not one (R11-3). If the spacing and the site set are both fixed, the universe cannot expand. If sites are created, a creation law that reads only *changes* in the local stress makes every constant vacuum energy invisible to the expansion (R12-2, OPEN, conditional and homogeneous only).
6. **Set A (records as a classical metric) hit one theorem.** For every stationary, homogeneous linear model in a broad class, "matter noise finite" and "metric record finite near the light cone" cannot both hold (R12-4, DERIVED). What survives needs a start time or a leaky (damped) gravitational wave.

**[S14 reading], the one-sentence picture.** Exact relativity for matter is solved inside the box, and the campaign can now say what any cure for the loops must contain (both statistics, per observable). It has not found a cure that reaches the electron, a mechanism that produces the graviton, or an untuned Λ beyond a homogeneous toy.

### 1.1 The C-box matter ladder (rung 4 now in d = 3)

- **R11-4: PASS WITH SCOPE [ref; `TESTS:4425-4436`; `vR11-4:23`].**
  - Conditional on the refereed d = 3 two-body BT box law and supplied minimal coupling to prescribed weak metric fields.
  - The stress is symmetric, Hermitian, Gevrey-quasi-local, with exact global energy conservation and box-to-box momentum conservation (off-box sources disclosed).
  - On the bound-triplet bundle the data fix every *projected* pole–dipole moment to the Newton–Wigner stress at linear spin; this is a projection, not the full stress (`vR11-4:5`).
  - **Von Laue is exact:** ∫T^ij = P_iP_j/h, zero at rest (`vR11-4:11`). Effective γ is binding-independent and equals the field's γ.
  - **Geodetic:** c(v) = Γ/(Γ+1) + γ, so (2Γ+1)/(Γ+1) → 3/2 at γ = 1; unit Schiff frame dragging (`vR11-4:13-17`). The MPD force check is canonical plus literature, not a separate covariant-SSC calculation.
  - **Not fixed:** the energy quadrupole. A double-divergence improvement changes it freely without touching lower moments (`vR11-4:19`). Price P-Q (P56 below).
  - Excluded from the PASS: global-flux numerics, self-consistent gravity, off-sector dynamics, nonlinear gravity.
- **R11-6: INCONCLUSIVE (worker only; no FAIL claimed, so no referee required) [`TESTS:4326-4331`].** Three-body B, H_S, K_S were assembled; the algebra and trimer-mass flatness are exact by conjugation; the registered subtracted-tail measurement is resolution-limited (aliasing beyond r ≈ L/6). Matrix-free large-r data favour super-polynomial decay (ΔAICc +4 to +31, β ≈ 0.3–0.45), but that is not the registered observable.
- **[S14 reading]** Every refereed C-box matter result is now "exact on the box domain, with disclosed off-box sources". The matter side has no known wall left at linear gravitational order; its open items are N ≥ 3 tails, the quadrupole, and nonlinear gravity.

### 1.2 The edge anomaly: what is now proved about any cure

**R10-1: SUGGESTED, with derived parts [ref; `TESTS:4270-4278`; `vR10-1:17`].**
- In free, separable Z³ × ℝ Peierls-coupled box theories, the scalar-QED photon-speed correction is exactly a positively weighted moment of A = Hess(ε²/2) − I. The Dirac correction is a moment of four functions (a, A, c₁, c₂). So "everything is an A-moment" is false for Dirac matter.
- **Theorem P [ref, with qualifications].** For Clifford-flat unit-speed bands and *matched masses*, fermion and scalar contributions cancel the photon coefficient pointwise for every edge shape. The actual 8-component fermion needs **four** complex scalars, not two (`vR10-1:7`). Unequal masses leave O(m_s² − m_f²).
- **What pairing leaves [ref].** The paired electron speed is δc_e·16π² = −10.66 (box curve) to −17.96 (Wilson curve) (`vR10-1:9`). Since the paired photon coefficient is zero, this is the electron–photon split.
- **Untuned? [ref].** Narrowly yes for the photon coefficient, under "one structural rule, no per-observable fit"; but equal curves, multiplicities and masses are imposed, not protected by a constructed symmetry (`vR10-1:13`).
- **"Six tunings" is not established** (`vR10-1:15`). The one-loop count for C and C-box is unknown.

**R11-1(a): DERIVED in the stated class [ref; `TESTS:4394-4400`; `vR11-1:23`].**
- **Theorem N\*.** Finitely many species in 𝒞_A, affine mass-squared families, nonnegative longitudinally independent nonvanishing weights: cancellation on an open mass interval forces the aggregate A-weighted boson and fermion measures to cancel *separately for each observable*. Bosons contribute negative totals, fermions positive (`vR11-1:3`). So neither statistics alone can do it. It does **not** force one-to-one species pairing.
- **Theorem S** (one curve, monotone, no doubler, c_γ = 1; anomaly-onset and parity hypotheses explicit): u = v is forced, and the TT condition forces w = 2√(N_F/N_B)S², i.e. w = S² for the four-scalar/eight-component unit (`vR11-1:9`).

**R10-5: FAIL (bounded) on clause 1, to class 𝒮 [ref; `TESTS:4303-4310`; `vR10-5:15`].**
- 𝒮 = canonical C¹, translation-invariant SUSY-QM/Nicolai class without quadratic gauge–scalar mixing.
- The matter multiplet works: exact free supercharge, zero matched vacuum energy.
- **The photon does not.** The three-component gauge Hessian must carry helicity Chern number ±2, which forces an extra transverse zero: no doubler-free box photon in 𝒮 (`vR10-5:7`).
- The stipulated TT pairing cancels the one-loop TT response for matched unit-speed curves; coupling "through Q" stays Lorentz-violating.
- The tested partner loops *enlarge* the electron–photon split (totals −15.5 to −20.95), but this is not a class-wide sign theorem (`vR10-5:11`).

**R12-3: INCONCLUSIVE, not bounded FAIL [ref; `TESTS:4483-4489`; `vR12-3:13`].**
- **BF is a genuine doubler-free gauge-quotient multiplet** on Z³ × ℝ: C² = ΔP_phys, c₁ = 0, nilpotent Q, Ward identity to 4.7e-16 (`vR12-3:5`).
- **But** its charged quotient Hamiltonian is Coulomb-nonlocal (an inverse orbit Laplacian), and no local equivariant completion or one-loop electron–photon split was built.
- The c₁ = ±2 obstruction needs conserved fermion number, not merely ghost U(1)_R (`vR12-3:3`). Theorem U excludes untwistable spin-½ photinos only in the narrow SO(3)-linear Nicolai class (`vR12-3:7`).
- **Theorem L, as refereed:** rescaling the gauge superpotential keeps Q exact and the Ward identity intact and moves c_γ/c_e freely, so the single Nicolai Q does not enforce c_γ = c_e. It does **not** prove that no lattice supersymmetry can relate them; Groot Nibbelink–Pospelov need the full supercharge–translation algebra (`vR12-3:9`).
- **[S14 note on the R12-6 registration.]** R12-6(e) quotes "Theorem L says no lattice supercharge fixes c_γ/c_e" (`TESTS:4503`). That is the worker's wording. The refereed scope is the single Nicolai Q only (`vR12-3:9`). R12-6(e) should be read against the narrow statement.

**Prior art the electron–photon question must count (not new, but it closes one "untuned" route).** IR running is too slow: for F2's realization the verified one-loop flow takes the split from 8.55e-3 at the cutoff to 7.34e-3 at 1.4 PeV, missing photon survival by 2.76e16 (C4 lane RE, E2: FAIL bounded, `TESTS:1543-1547`). Strong-coupling attraction makes relative *matter* speeds irrelevant only at a Lorentz-invariant fixed point with no vector deformation of dimension 3–4 (E1, `TESTS:1527-1538`).

**[S14 reading] Where the electron–photon split stands.** Nothing removes it without tuning.
- Minimal box QED: unsuppressed (R8-5, bounded FAIL).
- Cheapest non-minimal: strongly rejected (R9-8).
- Photon-only pairing: leaves −10.7 to −18.0 (R10-1).
- SUSY in 𝒮: photon doubler (R10-5).
- Twisted BF: doubler-free but Coulomb-nonlocal, split uncomputed (R12-3).
- Single nilpotent Q: does not tie the speeds (R12-3).
- IR running: too slow by ~1e16 (C4 E2).
- **Named candidates left:** the N=4 Kähler–Dirac completion (R12-6, running); a superalgebra that contains momentum (R13-1 below, the loophole in vR12-3:9); and whether BF's Coulomb term is physical or constraint-solving (R13-4 below).

### 1.3 The graviton

- **R11-2: EXCLUDED in the X1 class; (a) SUGGESTED [ref; `TESTS:4407-4415`; `vR11-2:17`].**
  - X1 = exact, locally finite, pairwise-commuting finite-slot N-type constraints whose averaged sector Hamiltonian has the regular lifted compact-character expansion and a nonsingular smooth linearization. There, every small-field frequency is O(k³). No light-like TT branch.
  - **A box symbol cannot help:** if d(q) = q near zero it cannot change the infrared vanishing order (`vR11-2:13`).
  - **Weinberg–Witten:** the brick-wall boost stays inside a momentum ball, so a box edge alone is no escape; WW binds a composite only when all its premises hold (`vR11-2:5`).
  - **X2 is not supported:** exact sourced constraints do not by themselves freeze mobile matter; a two-site counterexample transports the source (`vR11-2:11`).
  - Open routes O1–O6: emergent constraints, non-regular/strong-coupling phases, O(κ²) non-abelian algebras, instantaneous long-range couplings, mixed integer/compact slots, Goldstone tensor modes (`C5_R11-2_report.md:45-51`).
- **R12-1: INCONCLUSIVE; Theorem K's global sufficiency NOT CONFIRMED [ref; `TESTS:4477-4482`; `vR12-1:15`].**
  - *Necessity holds:* for free number-conserving box fermions on a smooth compactly supported core, exact Poincaré closure is necessary for degree-2 matter-bracket closure.
  - *Local statement:* within the fixed completion ansatz, an off-box O(q) Killing defect needs a 1/|q| singularity, i.e. a **1/r^{d−1} tail**.
  - *Common cone (conditional):* if one completed algebra had one flat structure function multiplying the whole momentum constraint, gravity and matter would need c_g² = c_m². That algebra is unbuilt (`vR12-1:9`).
- **R11-1(b): SPLIT-PRESENT in prescription dD-M only [ref; `TESTS:4401-4405`; `vR11-1:17-19`].**
  - c_m² − 1 = 4κm²J₂ on shell; the split is nonzero on both edges and both polarizations, with no fixed sign on the gapped edge; for light matter it tends to −κΞ.
  - Gauge-, Ward-completion- and square-root-prescription-dependent. Not a class-wide prediction.
  - **One existential fact survives any prescription:** Ξ_T2g ≠ Ξ_Eg, so a scalar matter cone can coincide with at most one graviton polarization's cone (`vR11-1:19`).
- **[pending] R12-5 (worker OPEN; `TESTS:4543-4551`).** The worker reports that sharp constraints kill the non-invariant terms Gu–Wen's linear mode needs (Lemma DW-q), one exact constraint caps TT at k², the soft energetic Gaussian is unstable, and the only window left is compact, non-Gaussian, stabilized phases. Exact diagonalization is infeasible (≥ 140 logical qubits). None of this is a verdict.

### 1.4 Λ

- **R11-3 (fixed grid): CONFIRMED WITH CORRECTIONS [ref; `TESTS:4417-4423`; `vR11-3:85`].**
  - **The tadpole identity:** with supplied free bands and the U stress vertex, ρ + p_U = −⟨ε tr A⟩/6 exactly (`vR11-3:26`). The vacuum's departure from w = −1 is an edge-supported anomaly moment: the same A as Theorem E (`TESTS:3556`).
  - **w ≥ 0** for U for every positive dispersion; for M only with nonnegative spatial kinetic contribution (`vR11-3:41`). A grid vacuum is radiation-like, not a cosmological constant.
  - **V1 (spacing grows): SOURCED,** two independent tadpole renormalization conditions (ρ and p) in the linear preferred-time EFT. A covariant Λ√−g counterterm moves only along (1, −1), so it cannot make Minkowski stationary alone. If nonlinear diffeomorphism invariance is imposed, the second counterterm is unavailable and this becomes an obstruction; exact signed spectral pairing could cancel both (`vR11-3:47`).
  - **V2/V3 (fixed √h per site): EXCLUDED as fixed-site cosmologies** (no isotropic expansion). V3 absorbs constant energy and pressure into integration data C(x), f(t) at linear order (`vR11-3:51,57`).
  - **Correction:** the "edge tuning" root is an infinitesimal small-mass result; the finite m: 1 → 0.3 step has no w = −1 point in the tested family (`vR11-3:63`).
  - Cutoff estimate at a = ℓ_P: 5.9e87 ρ_Λ, conditional, quadratically cutoff-sensitive (`vR11-3:65-73`).
- **R12-2 (site creation): OPEN [ref; `TESTS:4509-4517`; `vR12-2:17`].**
  - Under V3 with fixed proper site density, flat FRW slicing, timelike site worldlines and homogeneity, number balance forces **mean creation c̄ = 3H**; Friedmann behaviour is chosen through the creation law, not derived (`vR12-2:5`).
  - **The F-law (price P-T):** a derivative (Prony) rule reconstructs every w ≠ −1 density and annihilates every constant one. Late Λ_eff = 0 untuned, and a true Λ does not gravitate (`vR12-2:7`).
  - **Limits:** transitions leak into higher moments (m₂ = 16ρ_r + 9ρ_m − 4Δs′; 0.9% and 2.2% central errors); the runner hard-codes its memory evolution; no local 3D encoder, bound structures, inhomogeneous completion, source bridge or dark-energy sector.
  - **P-T is a genuine third conditional class** beyond "fixed C" and "vacuum-tracking C", not derived from the axioms (`vR12-2:13`).
- **R10-4 (set A, records as q-charge): OPEN [ref; `TESTS:4297-4301`; `vR10-4:27`].** With a supplied additive record-history 3-current, ε(*F) gives the Gibbs–Duhem stress, but the shift symmetry conserves μ: Minkowski after an electroweak step needs μ chosen for the final vacuum to a relative tolerance of 2.1e-55. That minimal realization is excluded; membrane, dissipative, global, count-dependent, q-coupled-matter and multi-flux completions are not.
- **[S14 reading]** On every grid set the vacuum question and the edge anomaly are now one question twice over: the vacuum's w ≠ −1 *is* an A-moment (R11-3), and the only structure seen to cancel A-moments is boson–fermion pairing (R11-1, O3 `TESTS:2399-2404`). The only untuned zero found anywhere is P-T, which works by making constants invisible rather than by cancelling them.

### 1.5 Set A: records as the classical metric

- **R10-3: EXCLUDED in class T_E [ref; `TESTS:4287-4295`; `vR10-3:19`].** Exact emission cancellation forces the metric-record covariance to be non-locally-finite at the cone. The "unread, non-gravitating record" rescue is incoherent with "records are the metric" (`vR10-3:13`).
- **R11-5: OPEN (not VIABLE) [ref; `TESTS:4438-4445`; `vR11-5:22`].** Lemma C: in the stationary class T_u, D′₀ + a²P_J/s² ≥ a|F|/|s|. The four-stage QND meter chain is confirmed; the full regulated kernel lacks a causal finite-start dilation. **A finite frame age is allowed as a named price** (`vR11-5:18`). 4e-7 to 5e-6 m is a conditional search interval, not a window (`vR11-5:12`).
- **R12-4: DERIVED [ref; `TESTS:4518-4525`; `vR12-4:19`].**
  - Class 𝒰: every translation-stationary, spatially homogeneous, linearized record-metric CQ theory at second order whose record obeys the nondemolition Kubo or additive product bound, whose metric response keeps an undamped massless 1/s pole, and whose gain is bounded away from zero on a one-sided regular cone patch.
  - **σ̄M ≥ κg²f₀²/s²:** matter noise and metric-record covariance cannot both be locally finite, in any nonsingular frame. The bound is state-independent, so it covers non-Gaussian stationary states (`vR12-4:5`).
  - 𝒰 contains T_E, T_u and R8-3's retained subclass.
  - **Not proved:** that every escape needs "a preferred frame plus exactly one regulator" (`vR12-4:15`). A start time is a temporal boundary, not a violation of "No site is privileged" (`AX:40`; `vR12-4:15`).
  - **E2 (GW friction)** is a plausible spectral escape, not a constructed CQ model. At γ = H₀, β = 2.26e-4 Mpc⁻¹, below the 6.75e-4 Mpc⁻¹ bound (`vR12-4:13`). **[pending] R12-7** constructs it.
- **[S14 reading]** Set A's covariant "records are the metric" is now pinned to the premises of 𝒰: it must give up stationarity (a start time), the undamped 1/s pole (GW friction), homogeneity, linearity, or the nondemolition product bound. Newtonian set A (R6-4) is unchanged.

### 1.6 Set B

- **R10-2: FAIL (bounded) on the OS-positivity clause [ref; `TESTS:4280-4285`; `vR10-2:23`].** Smooth box covariances fail site and link reflection positivity; no nonconstant smooth periodic O(4) two-point function is exact on an open box. Whole-zone SLAC is link-RP but has negative transfer spectrum down to −1. Without RP the count falls from 11 to 5 + Λ, not 2. R2-1 is not re-derived.

### 1.7 Calibration of S11's expectations [S14 reading]

- **Right:** R11-1(a) DERIVED (but aggregate, not pairwise); R11-3 V1 SOURCED with two conditions, V3 DECOUPLED and excluded on expansion; R11-5 OPEN; R11-6 INCONCLUSIVE; R11-2(a) SUGGESTED.
- **Better than expected:** R11-4 PASS WITH SCOPE (S11 said INCONCLUSIVE was likely). R11-2 reached a refereed EXCLUDED in X1 rather than OPEN.
- **Wrong:** R11-1(b) "sign-definite on the gapped edge" (no fixed sign, `vR11-1:23`). R11-3 V2 "sourced through the lapse" is right only for the energy constraint; the homogeneous pressure is absorbed (`vR11-3:51`).
- **Missed:** the R11-2 registration's PRODUCED clause required an all-orders Ward-exact coupling, which X2's worker argued is unreachable at O(κ) (`C5_R11-2_report.md:280`). A registration artefact of the R9-3 kind, though X2 was not confirmed.

---

## 2. The wall map

"Wall" = the refereed statement that stops the route. "Cheapest named price" = the least expensive price on record that passes it; "none named" means no price is known that passes it. Nothing here is adopted.

| Route | Refereed wall (scope) | Cheapest named price to pass it | Status of the price |
|---|---|---|---|
| **C-box, no pairing** | Theorem E zone identity, ⟨A_ii⟩_edge = −1/f_edge (`TESTS:3556`; `vR9-1:18`) plus charge rigidity (Lemma C `TESTS:3808`; Lemma Q `TESTS:3841`): loops integrate the edge. Photon split unsuppressed (R8-5, bounded); graviton speed an A-moment (R9-9); vacuum w ≠ −1 an A-moment (R11-3) | Per-observable counterterms: the e–γ relative speed (~3.1e-17 in F2, `TESTS:2380`), at least one graviton polarization (`vR11-1:19`), two vacuum tadpoles (`vR11-3:47`). I.e. set C's prices | Count not established (`vR10-1:15`). R11-1 Theorem N\* shows no untuned single-statistics choice exists in 𝒞_A |
| **C-box + pairing (C-box-S)** | (i) Pairing is necessary per observable (N\*), but the photon multiplet in 𝒮 has a doubler (Chern ±2, `vR10-5:7`); (ii) BF is doubler-free but Coulomb-nonlocal (`vR12-3:5`); (iii) the electron is left at −10.7 to −18.0 (`vR10-1:9`); (iv) a single nilpotent Q does not tie c_γ/c_e (`vR12-3:9`) | P46 (pairing unit) + P47 (a non-𝒮 photon multiplet) **plus** an e–γ counterterm (P48). So pairing buys the photon coefficient, the matched vacuum energy and (stipulated) TT, not the electron | Pending R12-6 (N=4 KD). Unpriced loophole: momentum in the superalgebra (R13-1) |
| **Set C, tuned** | No structural wall; the cost is the count. IR running is too slow (C4 E2, `TESTS:1543-1547`) | F2's 3.1e-17 e–γ counterterm; graviton and tadpole conditions as above; Λ to ~1e-123 twice on a fixed grid (V1) | Count unestablished |
| **Set A, CQ metric (covariant)** | 𝒰 no-go: σ̄M ≥ κg²f₀²/s² (`vR12-4:19`) | One 𝒰 premise must go. Named: a start time (P-r11a; allowed in principle, `vR11-5:18`) or frame-tied GW friction (P-r12a; R12-7 pending). Either keeps a regulator-dependent log-squared trade (`vR12-4:19`); worker L ≈ 72–84 (`C5_R12-4_report.md:172-188`) | Neither constructed. R11-5's finite-start dilation is missing (`vR11-5:9`) |
| **Set A, Newtonian** | None new (R6-4 VIABLE, `TESTS:3409-3418`) | R6-4's prices | Unchanged |
| **Λ, set A q-charge** | Minimal conserved-μ: needs μ fixed by the final vacuum to 2.1e-55 (`vR10-4:27`) | Q4: the final-vacuum datum (= R5-3's Λ6), or Q5: membranes, multi-flux, whole-history count, thermostat | All OPEN |
| **Λ, fixed grid V1** | Two independent tadpole conditions; w ≥ 0 (`vR11-3:79`) | Two tunings, or exact signed B/F pairing on identical bands (`vR11-3:47`) | Pairing route shares C-box-S's walls |
| **Λ, fixed grid V2/V3** | EXCLUDED as fixed-site cosmology (`vR11-3:57`) | Site creation (P52) | OPEN law |
| **Λ, site creation + P-T** | Homogeneous only; transitions leak into higher moments; no inhomogeneous completion (`vR12-2:7,15`) | P52 + P53 (P-T), plus a dynamical dark-energy sector (a true Λ is invisible) | Conditional, untested beyond FRW |
| **Graviton production** | X1: O(k³) (`vR11-2:17`); box symbol cannot lower the IR order (`vR11-2:13`); nonlinear algebra unbuilt (`vR12-1:15`) | Supplied CCR graviton (P-N1, = S11's P41), or instantaneous 1/r couplings (P-N2). The unpriced window: compact non-Gaussian strong-coupling phase (R12-5 pending; R13-2) | No produced graviton anywhere |
| **Nonlinear gravity on the box** | Degree-2 closure needs exact Poincaré on the core; off-box Killing defect needs a 1/r^{d−1} tail in the ansatz (`vR12-1:15`) | The box (P12-1) for the core; for the off-box defect, power-law completions (P12-2) | Whether the tail is physical or constraint-solving: R13-4 |
| **Set B** | R10-2: smooth box symbols fail RP (`vR10-2:23`) | Give up RP (5 + Λ) or whole-zone SLAC (negative transfer spectrum) | As S11's P43, now refereed |

---

## 3. Price ledger delta since S11 (P46 onward; named only, none adopted)

S11 ended at P45 (`C5_S11_synthesis.md:220-232`). **Status changes:** P42 (edge supertrace) is now refereed with corrections: four scalars per eight-component fermion, matched masses, electron not covered (`vR10-1:7-9`). P43 (set B box symbols) is now a refereed bounded FAIL (`vR10-2:23`). Dropped as incoherent: R10-3's P-r10b, an unread non-gravitating record (`vR10-3:13`).

**Axiom lines.** Lattice `AX:37-41` ("points of the cubic lattice Z³" `:37`; "No site is privileged" `:40`). Qubit `AX:45-53` (M₂(C) `:47`; "No possibility is privileged" `:52`). Admissibility `AX:57-61` ("one fixed nearest-neighbor admissibility rule" `:57`); reading notes `:63-73`. Record `AX:77-83` ("Records form" `:77`; "records are permanent" `:80`). Qualification `AX:87-95` ("A law privileges no states" `:94`). Not a dynamics axiom `AX:116-130`. Open gates `AX:173-190` (formation rules `:182-184`; record-production dynamics `:185-186`; source/action `:187`; scale reference `:189-190`).

| # | Price (named only) | Axiom text touched | Set | What the refereed record says it buys or costs |
|---|---|---|---|---|
| P46 | **Pairing unit, refined (refines P42).** Per observable, aggregate boson and fermion A-weighted measures cancel (N\*). In the one-curve subclass: a common Clifford-flat curve, u = v, the TT weight w = S², four complex scalars per eight-component fermion, matched masses (residual O(Δm²)) | Qubit `AX:47`: bosons (infinite-dimensional) plus 8-component fermions per cell against one M₂(C); O3: a qubit site cannot hold both CCR and CAR (`TESTS:2402`) | C-box-S, and V1 vacuum | Buys the photon coefficient for every edge shape and matched vacuum energy (`vR10-1:7`; `vR10-5:15`). Does not buy the electron (`vR10-1:9`). Not symmetry-protected as built (`vR10-1:13`) |
| P47 | **A photon multiplet outside 𝒮.** Either accept a photon doubler (𝒮), or the BF quotient multiplet: 7 CCR + 7 CAR per site, integer-twisted-spin photinos, a Coulomb-type inverse-Laplacian term in the charged Hamiltonian; or the N=4 KD content (+2 CCR, +1 CAR; worker: six massless neutral scalars) | Qubit `AX:47` (site content, `C5_R12-3_report.md:243-247`); Admissibility `AX:57` only if "nearest-neighbor" is read as a range limit on dynamics, which `AX:116-130` do not support [S14 reading] | C-box-S | `vR10-5:7`; `vR12-3:5,7`. Buys a doubler-free photon (BF). Split uncomputed. R12-6 pending |
| P48 | **No momentum in the superalgebra (P-noP).** With a nilpotent scalar Q, c_γ/c_e is a free parameter; the e–γ counterterm (~1e-16–1e-17) remains a tuning even under exact SUSY | Admissibility `AX:116-130`: no dynamics supplied, so no superalgebra is supplied either | C-box-S | `vR12-3:9`; `vR10-5:9`. The escape (momentum in the algebra) is unpriced: R13-1 |
| P49 | **Graviton production menu.** Leave X1 by one of: noncompact canonical pairs on both sides (P-N1, the supplied CCR graviton); instantaneous positive 1/r couplings between curvature operators (P-N2); a non-regular strong-coupling compact phase (P-N3, unbuilt); an O(κ²) field-dependent constraint algebra (P-N4) | P-N1: Qubit `AX:45-53`; P-N2: Admissibility `AX:57`; P-N4: source/action gate `AX:187` (`C5_R11-2_report.md:254-262`) | All grid sets | `vR11-2:17`. Only P-N1 is known to give a light-like TT branch (at tree level, R9-9) |
| P50 | **Nonlinear closure tails.** Degree-2 closure needs exact Poincaré on the core (the box, P12-1); off the box, the completion ansatz needs a 1/r^{d−1} tail (P12-2). If one common structure function exists, matter and graviton share one cone (P12-3, compatibility only) | Admissibility `AX:57` (range), as P26a/P37 | C-box | `vR12-1:9,15`. Whether the tail is gauge or physical is open |
| P51 | **Fixed-grid vacuum.** V1: two tadpole conditions (ρ and p), or exact signed B/F pairing; a/ℓ_P dynamical, so the scale reference holds at one epoch (P-V1b). V2/V3: fixed √h per site (a reading on Lattice, which fixes sites and adjacency, not a metric), frozen lapse, static fields as integration data C(x), a separate pressure datum f(t) | Lattice `AX:37-41`; scale reference `AX:189-190` | C, C-box | `vR11-3:47,51,79-81`; `C5_R11-3_report.md:238-252` |
| P52 | **Site creation.** The site set grows at mean rate 3H: a dynamical defect network (sites no longer literally Z³) or non-local plane insertion (S1); a creation-rate law (S2); an isometric encoder (S3); freezing in bound regions (S5) | Lattice `AX:37` ("points of the cubic lattice Z³"), `AX:40`; formation/creation rates downstream `AX:182-184`; Record permanence `AX:80` for S5 | C, C-box | `vR12-2:5`; `C5_R12-2_report.md:276-286` |
| P53 | **P-T, temporal vacuum reference.** The creation law reads only time variations of local stress along site worldlines (Prony to order 2N) plus per-site memory. Every constant component, including a true Λ, stops driving expansion. Consequence S6: observed acceleration needs a dynamical (w ≠ −1) sector with its own scale | Source/action gate `AX:187`; "A law privileges no states" `AX:94` (P-T privileges time-constancy, not a state: worker reading, `C5_R12-2_report.md:283`) | C, C-box | `vR12-2:7,13`. Homogeneous only |
| P54 | **q-charge for set A (refines R5-3's Λ9).** Q1: an energy function ε(q) of record-formation density in gravity's action; Q2: a formation-rate law d(ε′(q)) = 0; Q3: inert vacuum records near Planck 4-density; Q4: the zero datum μ = μ₀[final vacuum]; Q5: membranes / multi-flux + selection / whole-history count / thermostat | Source/action `AX:187`; formation rate `AX:182-184`; "A law privileges no states" `AX:94` (Q4, a tension); Admissibility `AX:57` for global laws (Q5) | A | `vR10-4:9,27`; `C5_R10-4_report.md:289-297` |
| P55 | **Set A past 𝒰.** Drop one 𝒰 premise: a start time (P-r11a: the record-production law gains a time origin; a temporal boundary, not a privileged site, `vR12-4:15`) or frame-tied GW friction with an energy sink (P-r12a). Carried: driven meters (P-r11b), a preferred frame (P-r1, not proved universally necessary), the near-cone log-squared trade | Record-production dynamics `AX:185-186`; Record `AX:77-80` unaffected | A | `vR11-5:18`; `vR12-4:13-19`. R12-7 pending |
| P56 | **P-Q, the quadrupole.** Box bodies' energy quadrupole is not fixed by the stress data; fixing it needs a localization rule for interaction energy (a field carrier for binding) or a minimal-coupling principle | Source/action gate `AX:187` | C-box | `vR11-4:19`; `C5_R11-4_report.md:258` |
| P57 | **dD-M graviton coupling.** A de Donder-type box propagator and lattice minimal metric coupling: a law choice. In it the matter–graviton split is unsuppressed (→ −κΞ). In any prescription, birefringence leaves at least one polarization off the scalar matter cone; removal needs a per-polarization condition or the TT pairing w = S² | Source/action gate `AX:187` | C-box | `vR11-1:17-19`; `C5_R11-1_report.md:309-318` |

**[S14 reading] How the price structure shifted since S11.**
- **Matter** prices bought one more exact result (P56 is the only new matter price, and it is about a quadrupole).
- **Field** prices (P46–P48, P57) now have a lower bound: whatever cures the loops must contain both statistics per observable (N\*). The pairing price is necessary and, so far, insufficient.
- **Cosmology** acquired its first untuned mechanism (P53), at the cost of P52 (the Lattice text) and of making a true Λ invisible.
- **Set A** prices narrowed to "which 𝒰 premise to drop" (P55).

---

## 4. Owner decision memo (for Jon; options with prices; nothing adopted)

### 4.1 The question in one line [S14 reading]

Grid relativity is exact for matter, including bound spinning bodies in curved fields. Loops still bring the grid back, and the campaign has proved what a cure must look like (both statistics, per observable) without finding one that reaches the electron. Separately, every set still supplies the graviton by hand, and the only untuned zero for Λ works by making constants invisible.

### 4.2 Options

**Option A: continuum base, discreteness only in records.**
- *Buys:* exact Poincaré, one cone, exact equivalence principle, no LV tunings. Newtonian records-as-metric VIABLE on about 1e-10 to 5e-6 m (R6-4).
- *Pays:* the set-A axiom prices (`C5_S5_synthesis.md:94`); a supplied graviton; **to go covariant, one of 𝒰's premises (P55)**; Λ through a q-charge (P54) that needs a final-vacuum datum or an extra sector.
- *Open:* both 𝒰 escapes are unconstructed (R11-5's dilation; R12-7 running).

**Option C: keep the four texts and tune.**
- *Buys:* no text changes.
- *Pays:* the e–γ counterterm (~3.1e-17 in F2), at least one graviton-polarization condition, two vacuum tadpoles on a fixed grid (V1), F2's budget; a supplied graviton. The total count is not established.
- *Open:* the count.

**Option C-box: Z³, a box-exact law, qubits in a sector.**
- *Buys:* exact relativity for number-conserving matter inside a rapidity budget; exactly universal fall, von Laue, γ, geodetic 3/2 and Schiff for bound bodies (R9-2, R9-10, R11-4).
- *Pays:* S11's P26–P29, P35–P41, P45; plus P50, P56, P57. **At one loop it pays option C's conditions as well** (no refereed result removes any of them).

**Option C-box-S: C-box with boson–fermion pairing per cell.**
- *Buys:* the photon's one-loop shift (Theorem P), matched vacuum energy, the TT response with w = S² (stipulated vertex).
- *Pays:* P46–P48; P47's choice between a doubler, a Coulomb-type term, or N=4 content; **and still the e–γ counterterm** unless R12-6 or R13-1 changes that.
- *Open:* the electron. Everything rides on R12-6 and on whether momentum can be put into a lattice superalgebra.

**Cosmology overlay (any grid option).**
- *V1:* spacing grows; two tadpoles; a/ℓ_P dynamical.
- *Site creation + P-T:* untuned late Λ_eff = 0 (homogeneous only); a true Λ is invisible, so dark energy must be dynamical with its own scale.

### 4.3 Questions only Jon can answer

1. **Start time or leaky gravity (set A).** If set A, which is acceptable: a law with a beginning (records start forming at a finite time; the record-production law gets a time origin, `AX:185-186`), or gravitational waves that lose energy to the frame at a rate near H₀ (needs an energy sink)? Or neither, which leaves set A Newtonian only (R12-4 DERIVED).
2. **Pairing per cell.** Pairing is now *necessary* for untuned cancellation in 𝒞_A (R11-1). Is a graded cell (bosons plus eight-component fermions) a price you would consider against "one-site possibility domain M₂(C)" (`AX:47`)? If no, the grid options are tuned options.
3. **Sector selection (P45).** Is a flux-free qubit sector, selected by hand or by an unproved gap, acceptable as "the physical sector" (`AX:52,94`)?
4. **Temporal vacuum reference (P-T).** Can a law read *changes* in the local stress, so that anything constant, including a true Λ, does not drive expansion? Is "the law privileges time-constancy" consistent with "A law privileges no states" (`AX:94`)?
5. **Site creation (P52).** May the site set grow (`AX:37`: "Physical sites are the points of the cubic lattice Z³")? Without it, a fixed grid with fixed volume per site cannot expand (R11-3); the alternative is growing spacing (V1) with two tadpoles and a drifting a/ℓ_P.
6. **Range.** Is a law with super-polynomial (box) tails acceptable, and is a 1/r^{d−1} constraint-solving tail acceptable if it turns out to be gauge, like the Coulomb term in QED (R13-4)?
7. **Tuning.** Is a tuned e–γ relative-speed counterterm at the 1e-17 level an acceptable price, given that nothing untuned has been found?

### 4.4 Honestly open whichever option is chosen

- **Producing the graviton.** Nothing produced in any set. X1 excluded; the compact non-Gaussian window is uncomputed (R12-5 pending).
- **The electron–photon split.** No untuned mechanism. R12-6 is the last registered lattice-SUSY route.
- **Λ's mean.** One conditional homogeneous mechanism (P-T). Everything else is a datum or a tuning.
- **Nonlinear gravity on the lattice** (R12-1 INCONCLUSIVE). **N ≥ 3 tails** (R11-6 INCONCLUSIVE).
- **The one-loop tuning count** for C and C-box (`vR10-1:15`).

---

## 5. Draft round-13 pre-registrations (readings fixed before any run)

**Rules (as rounds 2–12).** Probes: Opus 5.5 at xhigh. Every FAIL, EXCLUDED or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded. Prices are named, never adopted. Each probe greps the repository and packet for prior art first and counts each match once. Hypotheses before titles; excluded outside realizations listed. Numbers from memory labelled RECALLED. Every tail or decay clause names its subtraction before any run (R9-3 rule). **New rule (from R11-2's registration):** a PRODUCED or PASS clause names the perturbative order at which each exactness condition is required.

**Overlap check.**
- R12-6 builds the twisted N=4 Kähler–Dirac multiplet with a nilpotent scalar Q and computes c_e − c_γ there. R13-1 uses *untwisted spinor* supercharges whose square contains momentum; it excludes twisted and nilpotent-scalar classes. R13-4(i) asks about BF *without* σ, η; launch part (i) after R12-6(a) reports, and drop it if R12-6 supplies a local completion.
- R12-7 builds set A's GW-friction route (E2). R13-6 builds the start-time route (E1), so the owner has both sides of question 1. No overlap.
- R12-5 is the strong-coupling graviton argument. R13-2 is a numerical Euclidean test of the same window; launch after R12-5's referee.
- R13-3 and R13-5 overlap nothing running.

**Priority.** R13-1, R13-2 (after R12-5's referee), R13-3, R13-4, R13-5, R13-6 (pair with R12-7's result).

---

**R13-1. The electron–photon split: momentum in the superalgebra on the box.**

- **Plain question.** The theorem that supersymmetry forbids dimension-4 Lorentz violation (Groot Nibbelink–Pospelov) needs supercharges whose square is the momentum. On a lattice no local difference operator obeys the product rule (Kato–Sakamoto–So), so lattice superalgebras leave momentum out, and then nothing ties the electron's speed to the photon's (`vR12-3:9`). But the box symbol is exactly linear inside the box, so the product rule holds whenever all momenta, and their sums, stay in the box. Can a supercharge with {Q, Q̄} = 2σ·P exist on box states, and does it force c_e = c_γ at one loop, even though loops reach the edge?
- **Setting.**
  - Z³ × ℝ, Hamiltonian. A free chiral multiplet and an abelian vector multiplet with untwisted spinor supercharges Q_α. Box symbols p_i(k) = k_i on the open box B, smooth and periodic outside; Ward-forced gauge coupling on the whole zone (Lemma C).
  - Two domains: (D1) the box-additive domain (all external and internal momenta and their sums in B); (D2) the full zone with a periodic p(k).
  - Excluded: twisted or nilpotent-scalar-Q constructions (R12-3, R12-6); class 𝒮 (R10-5); interactions beyond one loop.
- **Prior art (count once).** C4 F2's "SUSY fails (suggested)" and its referee correction that Kato–Sakamoto–So has infinite-flavour/non-local escapes (`agents/C4_F2_referee.md:46`); C4 P1 referee on KSS and FS models; R10-5 Lemma J (`vR10-5:9`); R12-3 Theorem L and its scope (`vR12-3:9`); R11-1 Theorem N\*; R8-2/R9-2 box-to-box momentum conservation; KSS 0803.3121, 0810.2360; GNP hep-ph/0404271; Dondi–Nicolai 1977; Bergner et al. on SLAC-derivative SUSY (RECALLED).
- **Probes.**
  - (a) **Free level.** Construct Q_α with {Q_α, Q̄_β} = 2σ^μ_{αβ}P_μ on D2. Prove or refute: the algebra forces one common p(k) for every multiplet coupled to the same P (one cone at tree level by algebra, not by tuning).
  - (b) **Interacting.** Add the gauge and Yukawa vertices. State on which domain the superalgebra closes. Give the defect operator off D1 explicitly.
  - (c) **One loop.** Compute c_e − c_γ in minimal box SQED (electron, selectron, photon, photino) with matched masses, on the literal and gapped edges. Is it zero, or an edge moment of the product-rule defect? Give the number in e²/16π² units and the residual under a mass split O(Δm²a²).
  - (d) **Doublers.** Does the vector multiplet have a doubler (R10-5's Chern ±2 argument is for 𝒮)?
  - (e) Per-site content and prices.
- **FIXED readings.**
  - **PASS:** an explicit law with spinor Q, {Q, Q̄} = 2σ·P exact on a stated domain, a Ward identity, a doubler-free photon, and one-loop c_e − c_γ = 0 for every edge shape at matched masses (residual O(Δm²a²) stated), checked.
  - **FAIL:** a refereed no-go: in a stated class containing box-symbol spinor SUSY, either a photon doubler is forced, or the one-loop c_e − c_γ equals a nonzero edge moment of the product-rule defect that no untuned choice removes.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** (a) a common p(k) is forced at the free level. (b)–(c) the product-rule defect lives exactly where the edge anomaly lives, so supersymmetry fails in the loop and the split becomes a defect moment: INCONCLUSIVE leaning FAIL. The upside, if the defect moment cancels by N\*'s structure, would be the campaign's first untuned removal of the electron–photon split.

---

**R13-2. Producing the graviton: the compact non-Gaussian window, by Euclidean Monte Carlo.**
*(Launch after R12-5's referee. Use whatever of Lemma DW-q, X1-E and the Gaussian-instability statement is confirmed; otherwise state them as hypotheses.)*

- **Plain question.** Exact qubit constraints give gravitons with ω = O(k³) (X1). The R12-5 worker says one exact constraint caps them at k², the soft Gaussian version is unstable, and the only window left is a compact, strongly coupled phase where both constraints are energetic. Exact diagonalization cannot reach it. But a Euclidean path integral of a compact (Villain-type) model is a classical 4D statistical model. If its weights are positive, Monte Carlo can measure the tensor correlator directly and read off how frequency scales with momentum. Is there a phase with light-like (z = 1) gravitons, two polarizations and nothing else gapless?
- **Setting.**
  - A rank-2 symmetric-tensor U(1) or Z_N gauge field with integer conjugates on Z³, both N-type constraints imposed energetically; Euclidean Z³ × Z_τ by Trotter/Villain; L from 6 up to the largest feasible (target ≥ 12), at least three sizes.
  - Excluded: matter, nonlinear gravity, Λ.
- **Prior art (count once).** R11-2 and verdict (X1, Lemma A_c, dressing law; `vR11-2:7-9`); R12-5 (pending; `TESTS:4543-4551`); N0914 (Gaussian instability); lane R (`TESTS:685-776`); Gu–Wen 0907.1203 (they call the linear N-type result unreliable; `vR11-2:9`); Xu 2006; Pretko 2017; published Monte Carlo of rank-2 U(1) Coulomb phases (RECALLED; verify before use).
- **Probes.**
  - (a) Write the Euclidean Villain form. Prove positivity of the weights, or locate the sign problem (expected in the trace/conformal sector).
  - (b) If positive: sample a coupling grid that includes U ~ J ~ g. Measure the TT, vector and scalar correlators G(ω_n, k); extract z from a pre-registered collapse fit; count gapless polarizations; detect confinement.
  - (c) If not positive: give the cheapest sign-free deformation and state which constraint or which polarization content it changes.
  - (d) Prices.
- **FIXED readings.**
  - **PRODUCED:** a phase with z = 1 ± 0.1 by the pre-registered collapse fit on ≥ 3 sizes, exactly two gapless TT polarizations, no gapless vector or scalar partners, checked.
  - **EXCLUDED:** a refereed no-go in a stated class (for example, positivity forces confinement, or z ≥ 2, or gapless partners).
  - **OPEN:** otherwise, including an unresolved sign problem.
- **Expectation.** OPEN. Most likely a sign problem in the trace sector; if sign-free, a confined phase at strong coupling and a weak-coupling phase with k² or k³ modes or gapless partners. A clean z = 1 two-polarization phase is not expected; a definite numerical answer either way would still close or open the last unpriced window.

---

**R13-3. Λ: the P-T creation law in a lumpy universe (inhomogeneous completion, bound regions, phase transitions).**

- **Plain question.** R12-2 found a homogeneous rule that creates sites at mean rate 3H and reads only *changes* in the local stress, so constant vacuum energy cannot drive expansion. It has never been written for a universe with galaxies, sound waves and phase transitions. Do bound systems stay unexpanded without a clamp? Does a phase transition leak a visible energy density? And in V3 the static field is an integration datum C(x), which behaves like extra dust (Mukohyama's "dark matter as integration constant"): is that a defect or a feature?
- **Setting.**
  - V3 (fixed √h per site, fixed lapse) with site creation obeying a local 3D F-law (P53): creation density c(x, t) a functional of time derivatives of local stress along site worldlines, plus finitely many per-site memory variables, with a stated local encoder.
  - Linear perturbations about FRW; a top-hat collapse to a virialized region; a first-order phase transition **with a specified transition sector** (the ingredient missing in R11-3, `vR11-3:55`).
  - Excluded: records as a q-charge (R10-4); the pairing route.
- **Prior art (count once).** R12-2 and verdict (`vR12-2:5-17`); R11-3 and verdict (`vR11-3:51,57`); R10-4 Q1–Q5; R5-3 Lemma PT (`TESTS:2985-2993`); O3 P13; Mukohyama 2009 (cited `C5_R11-3_report.md:97,185`; RECALLED); RN L3 (projectable Hořava strong coupling); Perlman et al. 1411.7262 on foam (`vR12-2:11`); DESI DR2 w₀w_a (comparator).
- **Probes.**
  - (a) Write the local 3D rule and encoder. Show c̄ = 3H is recovered on average.
  - (b) **Linear perturbations.** Growth D(a) and the ISW source. Does C(x) behave as pressureless dust with zero sound speed? What sets its amplitude?
  - (c) **Bound regions.** In a virialized top-hat, is the creation rate zero inside without a clamp? What memory time does that need relative to orbital periods?
  - (d) **Phase transition.** Compute the leakage into higher Prony moments with the specified transition sector. Compare with ΔN_eff and early-dark-energy bounds (state the bounds used).
  - (e) **Acceleration.** A true Λ is invisible. State which sector produces today's acceleration, and whether the F-law makes it visible only through w ≠ −1.
  - (f) Prices.
- **FIXED readings.**
  - **VIABLE:** an explicit local 3D rule with (b)–(e) passing their stated comparators, bound regions non-expanding without a clamp, prices named, checked.
  - **EXCLUDED:** a refereed inconsistency in a stated class (for example, every local rule of memory order N creates sites inside virialized regions, or leaks more than the stated bound for every N).
  - **OPEN:** otherwise.
- **Expectation.** OPEN. Most likely: (c) forces a memory time at least the longest bound-orbit period, which makes the rule non-local in time; (d) leaks at roughly the latent-heat fraction (R12-2's 1–2%), dangerous only for late transitions; (b) C(x) acts as dust with unexplained initial data.

---

**R13-4. Tails: are the Coulomb-type tails of the BF photon multiplet and of the off-box gravity completion physical, or constraint-solving as in Coulomb-gauge QED?**
*(Part (i) launches after R12-6(a) reports; drop it if R12-6 supplies a local completion.)*

- **Plain question.** Two routes stopped at the same kind of term. The doubler-free BF photon multiplet has an inverse-Laplacian (Coulomb-type) piece in its charged Hamiltonian (`vR12-3:5`). The off-box gravity completion needs a 1/r^{d−1} tail (`vR12-1:15`). Ordinary QED in Coulomb gauge also has an instantaneous 1/r term, yet it is a local theory: the term only solves Gauss's law, and gauge-invariant observables respect the light cone. Are these two tails of that harmless kind, or do they act on physical observables at a distance? And, as a control, how big is the box law's own super-polynomial leakage outside the light cone?
- **Setting.**
  - (i) R12-3's BF quotient Hamiltonian with charged box matter.
  - (ii) R12-1's completion ansatz for the off-box Killing defect.
  - (iii) Control: R7-1's free box law and R9-5's qubit realization.
  - "Constraint-solving" means: there is a local Hamiltonian on an extended space with local constraints whose reduced dynamics equals the given one, so the tail appears only in gauge-dependent quantities.
  - Excluded: N=4 KD content (R12-6); interacting gravity beyond degree 2.
- **Prior art (count once).** R12-3 and verdict; R12-1 and verdict (`vR12-1:5,15`); R11-2 on Marolf's kinematic non-locality (`vR11-2:5`); C5_R12-1 P12-2 (`C5_R12-1_report.md:272`); R7-1 and R9-5 tail constants (`vR9-5:9,12`); R11-6's large-r fits (`TESTS:4330`); Coulomb-gauge QED and Lieb–Robinson bounds for quasi-local Hamiltonians (RECALLED).
- **Probes.**
  - (a) For (i) and (ii): construct a local extended formulation, or prove none exists in a stated class. Compute the equal-time commutator of gauge-invariant local observables at separation r and its decay.
  - (b) For (iii): the maximal group velocity over the whole zone, and the commutator leakage outside the cone versus distance from it, with constants, at a = ℓ_P (a reading on `AX:189-190`).
  - (c) Prices, against `AX:57` and `AX:116-130`.
- **FIXED readings (per object (i), (ii)).**
  - **LOCAL-EQUIVALENT:** an explicit local extended formulation, with gauge-invariant commutators decaying at least super-polynomially outside the cone, checked.
  - **PHYSICALLY NON-LOCAL:** a refereed proof that a gauge-invariant commutator decays no faster than a power, in a stated class.
  - **OPEN:** otherwise.
  - (iii) is reported as numbers with constants (no verdict).
- **Expectation.** (i) LOCAL-EQUIVALENT for the bosonic part, as in Coulomb-gauge QED; the photino/ghost sector may need the equivariant completion. (ii) OPEN. (iii) group velocity ≤ 1 achievable on the whole zone; leakage negligible at a = ℓ_P.

---

**R13-5. The graviton–matter split, gauge-invariantly: Ward-complete the pair-creating stress, then compute the pole positions.**

- **Plain question.** R11-1(b) found the matter and graviton cones split, but only in one prescription; the pair-creating stress was never Ward-completed (`vR9-9:5`; `vR11-3:31`; `vR11-1:19`). GW170817 says gravitons and light arrive together to about 1e-15. A prescription-independent number needs the missing piece: a Ward-complete pair stress. With it, compute the shift of the physical poles (which is gauge-invariant), with and without the TT pairing w = S².
- **Setting.** R9-9's N-type box graviton; R8-2's stress plus a pair-creating completion satisfying the second-order Ward identity; complex scalars and Clifford-flat fermions on the literal and gapped edges; m = 1 and 0.3; the paired unit of Theorem S as a variant.
- **Prior art (count once).** R9-9 and verdict (`vR9-9:5,23`); R10-5 Theorem PT (`vR10-5:5`); R11-1 (`vR11-1:9,17-19`); R11-3's U/M vertices (`vR11-3:31`); RFW (field-dependent Ward completion); GW170817 (comparator).
- **Probes.** (a) Construct the Ward-complete pair stress (or prove none exists in a stated class). (b) Compute the one-loop pole shifts of the TT graviton (both polarizations) and of scalar matter; give c_m − c_T in κ_lat units and its size at a = ℓ_P. (c) Repeat with the paired unit. (d) State which seagull terms the Ward identity fixes.
- **FIXED readings.**
  - **SPLIT-PRESENT:** a nonzero pole-position split for every Ward-complete stress in a stated class (refereed if claimed class-wide), with numbers.
  - **SPLIT-ABSENT:** the pole split vanishes identically for the Ward-complete stress (with or without pairing, stated), with the reason, checked.
  - **OPEN:** otherwise.
- **Expectation.** SPLIT-PRESENT without pairing (birefringence alone forces one polarization off the matter cone, `vR11-1:19`); with pairing, SPLIT-ABSENT for TT at matched unit-speed curves, with the scalar matter self-energy unpaired.

---

**R13-6. Set A, route E1: an explicit start-time CQ dilation (R11-5's missing piece).**

- **Plain question.** R12-4 proved that a stationary record-metric model cannot keep both matter noise and the metric record finite at the light cone. One escape is a law with a start time. R11-5 built the meter chain but not the full causal finite-start construction (`vR11-5:9,22`). Build it, so that the owner can compare "a start time" (this item) with "leaky gravitational waves" (R12-7) on equal terms.
- **Setting.** Linearized Gaussian CQ gravity with mean GR coupling, R11-5's regulated kernel family 𝒦_ε, a finite start t₀, a preferred frame (CMB), integer n ≥ 3. Excluded: GW friction (R12-7); non-Gaussian and jump models.
- **Prior art (count once).** R6-4; R8-3; R9-4; R10-3; R11-5 and verdict (`vR11-5:6-22`); R12-4 and verdict (`vR12-4:5-19`); `C5_R12-4_report.md:162` (E1 row).
- **Probes.** (a) Construct a positive synthesis measure, a causal spectral factor, the finite-start state and covariance, and the exact map from the meter bank to the displayed spectra; prove complete positivity. (b) Record growth (ε ln t, or linear with a finite regulator) and its size at t_H. (c) Re-run R11-5's tests, adding the nonlinear noise-fed PPN term. (d) The allowed ℓ_s interval, or none. (e) Prices.
- **FIXED readings.**
  - **VIABLE:** an explicit finite-start model passing every stated test on a stated ℓ_s interval, with prices named, checked.
  - **EXCLUDED:** a refereed inconsistency or bound violation for every ℓ_s in the class.
  - **OPEN:** otherwise.
- **Expectation.** OPEN, leaning VIABLE on a narrow interval near 4e-7 to 5e-6 m; the noise-fed PPN term is the likeliest failure point.

---

## 6. Caveats

- **Same family, unrefereed.** The option split, every "[S14 reading]", the wall map's "cheapest price" column, the price numbering P46–P57, the owner questions and the R13 drafts are S14's.
- **Pending.** R12-5's Lemma DW-q, X1-E and "only window left" are worker claims. R12-6 and R12-7 have no reports. If R12-6 builds a local N=4 completion with a vanishing split, §1.2's "nothing removes it", P47–P48, option C-box-S and R13-1/R13-4(i) must be revisited.
- **Bounded, not class-wide.** R10-5 is bounded to 𝒮; R11-2 to X1; R12-4 to 𝒰; R10-3 to T_E; R10-2 to its OS class. R11-1(a) is DERIVED only in 𝒞_A and at aggregate level. **No refereed result says the edge anomaly is unremovable in general** (`vR10-1:3`).
- **Prescription scope.** R11-1(b)'s numbers are dD-M only. R11-3's tadpoles assume the supplied U/M vertices and the linear N-type coupling.
- **Scale bridge.** Every Planck-unit statement (5.9e87 ρ_Λ, rapidity budgets, R13 sizes) uses a = ℓ_P, which the axioms leave open (`AX:189-190`).
- **The sets are not exhaustive.** Relational and non-commutative constructions are unexamined.
- **Drafts are proposals for the driver.** Readings are fixed here so they cannot be adjusted after a run. The driver may reorder or drop items.
